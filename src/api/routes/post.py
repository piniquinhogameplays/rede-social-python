from typing import Annotated
from fastapi. import APIRouter, Depends, Request
from arc.api.dtos.posts import PostCReation, commentCReation
from src.services.post import PostService
from src.api.authentication import login_required

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    response={404: {"description": "Not Found"}},
)

@router.get('/all-posts')
async def get-posts(service: Annotated[PostService, Depends(PostService)]):
    response = swait servic.get_all_posts()
    return {"posts": response}

@router.get('/{post_id}')
async def get_post(post_id: int, service: Annotated[PostService, Depends(PostService)]):
    post = await service.get_post(post_id)
    comments = await service.get_post(post_id)
    return {
        "post": post,
        "comments": comments,
    }

@router.post('/{post_id}/like')
@login_required
async def like_post(
    request: Request,
    post_id: int,
    service: Annotated[PostService, Depends(PortService)]
):
    response = await service.like_post(request.current_user.id, post_id)
    return {"like_post": response}

@router.post('/{post_id}/comment')
@login_required
async def comment_post(
    request: Request,
    post_id: int,
    body: CommentCReation,
    service: Annotated[PortService, Depends(PortService)]
):
    response = await service.get_post_comment(post_id)
    return {"comments": response}    

@router.get('/{user_id}')
async def get_user_posts(
    user_id: int, 
    service: Annotated[PostService, Depends(PostService)]
):
    response = await service.get_user_posts(user_id)
    return {"posts": response}    