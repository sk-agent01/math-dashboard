"""API routes for math operations."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.operations import OPERATIONS

router = APIRouter()


class CalculateRequest(BaseModel):
    """Request body for calculation endpoint."""
    operation: str
    params: dict[str, float | int]


class OperationInfo(BaseModel):
    """Schema for operation metadata."""
    key: str
    label: str
    description: str
    params: list[dict]


class CalculateResponse(BaseModel):
    """Response body for calculation endpoint."""
    operation: str
    result: str | int | float


@router.get("/operations", response_model=list[OperationInfo])
def list_operations():
    """List all available operations with their metadata."""
    return [
        OperationInfo(
            key=key,
            label=op["label"],
            description=op["description"],
            params=op["params"],
        )
        for key, op in OPERATIONS.items()
    ]


@router.post("/calculate", response_model=CalculateResponse)
def calculate(req: CalculateRequest):
    """Execute a math operation."""
    if req.operation not in OPERATIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown operation: {req.operation}. "
                   f"Available: {', '.join(OPERATIONS.keys())}",
        )

    op = OPERATIONS[req.operation]

    # Validate required params
    required = {p["name"] for p in op["params"]}
    missing = required - set(req.params.keys())
    if missing:
        raise HTTPException(
            status_code=422,
            detail=f"Missing parameters: {', '.join(missing)}",
        )

    # Extract only expected params
    kwargs = {p["name"]: req.params[p["name"]] for p in op["params"]}

    try:
        result = op["func"](**kwargs)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Calculation error: {e}")

    return CalculateResponse(operation=req.operation, result=result)
