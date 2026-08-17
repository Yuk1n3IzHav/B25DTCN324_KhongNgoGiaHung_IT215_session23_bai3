from fastapi import APIRouter, Depends, HTTPException, status

from data import resources
from dependencies import get_current_user, require_admin
from models import ResourceCreate, ResourceResponse

router = APIRouter(
    prefix="/resources",
    tags=["Resources"],
)


@router.get("", response_model=list[ResourceResponse])
def get_resources(
    current_user: dict = Depends(get_current_user),
):
    if current_user["role"] == "admin":
        return resources

    return [resource for resource in resources if resource["is_published"]]


@router.get("/{resource_id}", response_model=ResourceResponse)
def get_resource(
    resource_id: int,
    current_user: dict = Depends(get_current_user),
):
    resource = next(
        (resource for resource in resources if resource["id"] == resource_id),
        None,
    )

    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )

    # User không được biết resource chưa publish tồn tại
    if current_user["role"] == "user" and not resource["is_published"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )

    return resource


@router.post(
    "",
    response_model=ResourceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_resource(
    data: ResourceCreate,
    current_user: dict = Depends(require_admin),
):
    new_id = (
        max(
            [resource["id"] for resource in resources],
            default=0,
        )
        + 1
    )

    resource = {
        "id": new_id,
        "title": data.title,
        "description": data.description,
        "url": str(data.url),
        "is_published": False,
        "created_by": current_user["username"],
    }

    resources.append(resource)

    return resource


@router.patch(
    "/{resource_id}/publish",
    response_model=ResourceResponse,
)
def publish_resource(
    resource_id: int,
    current_user: dict = Depends(require_admin),
):
    resource = next(
        (resource for resource in resources if resource["id"] == resource_id),
        None,
    )

    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )

    resource["is_published"] = True

    return resource


@router.delete("/{resource_id}")
def delete_resource(
    resource_id: int,
    current_user: dict = Depends(require_admin),
):
    resource = next(
        (resource for resource in resources if resource["id"] == resource_id),
        None,
    )

    if not resource:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )

    resources.remove(resource)

    return {"message": "Resource deleted successfully"}
