from fastapi import APIRouter

from . import public


router = APIRouter(prefix = '/accounts')

router.include_router(public.router)
