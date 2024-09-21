

import json
import uuid
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

from app.core.dependencies import RabbitMQClient
from app.repositories.category_repository import CategoryRepository
from app.schemas.category_schema import CategorySchema


class CategoryService:
    async def create_category(data:CategorySchema, producer:RabbitMQClient):
        try:
            universal_id = str(uuid.uuid4())
            category_dict = jsonable_encoder(obj=data)
            category_dict["universal_id"] = universal_id
        
            new_catgory = await CategoryRepository.create_category(category_dict)
            
            result = await CategoryRepository.get_cagegory_by_id(new_catgory.inserted_id)
        except DuplicateKeyError:
            raise HTTPException(
                status_code=409, detail="Category already exists"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(object=e))
        else:
            # Update the data to include the universal_id
            data_with_universal_id = data.model_dump()
            data_with_universal_id["universal_id"] = universal_id
            await producer.publish("create_category", json.dumps(data_with_universal_id))
            return result
    
    async def get_categories():# -> list:
        categories = await CategoryRepository.get_categories()
        return categories