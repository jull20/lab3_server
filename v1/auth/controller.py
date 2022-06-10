from fastapi import Request, HTTPException, status
from sqlalchemy.orm import Session

from v1.auth.schema import RequestLoginSchema, RequestRegisterSchema, ResponseLoginSuccess, ResponseSuccess
from models import User

def _hash_password(password: str):
    return 'sec'.join(password)

async def login_service(db: Session, request: Request, loginBody: RequestLoginSchema):
    try:
        user: User = db.query(User).filter(User.email == loginBody.email, User.hashed_password == _hash_password(loginBody.password)).one()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong email or password')
    
    request.session.update({
        'user': {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'is_admin': user.is_admin
        }
    })

    return ResponseLoginSuccess(username=user.username, email=user.email, isAdmin=user.is_admin)



async def register_service(db: Session, request: Request, registerBody: RequestRegisterSchema):
    user = User(username=registerBody.username, 
                email=registerBody.email, 
                name=registerBody.name, 
                hashed_password=_hash_password(registerBody.password)
            )
    
    try: 
        db.add(user)
        db.commit()
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username or email already exist')

    request.session.update({
        'user': {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'is_admin': user.is_admin
        }
    })

    return ResponseLoginSuccess(username=user.username, email=user.email, isAdmin=user.is_admin)


async def logout_service(db: Session, request: Request):
    request.session.clear()

    return ResponseSuccess()