from sqlalchemy.dialects.postgresql import UUID as UUID_PG
from sqlalchemy.orm import relationship

from auth_server import db
from auth_server.functions.models import GlobalRole, Mode


class RefreshTokenOrm(db.Model):
    __tablename__ = 'refresh_tokens'
    token_id = db.Column(UUID_PG, primary_key=True, nullable=False)
    user_id = db.Column(db.String(63), nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True))
    expiration_date = db.Column(db.DateTime(timezone=True))
    is_revoked = db.Column(db.Boolean())


class UserOrm(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(63), primary_key=True, nullable=False)
    global_role = db.Column(db.Enum(GlobalRole))
    groups = relationship("UserGroupOrm")


class GroupOrm(db.Model):
    __tablename__ = 'groups'
    group_id = db.Column(db.String(63), primary_key=True, nullable=False)
    description = db.Column(db.String(255))
    users = relationship("UserOrm")


class UserGroupOrm(db.Model):
    __tablename__ = 'users_groups_roles'
    relation_id = db.Column(db.Integer(), primary_key=True, nullable=False)
    user_id = db.Column(db.String(63), db.ForeignKey('users.user_id'), nullable=False)
    group_id = db.Column(db.String(63), db.ForeignKey('groups.group_id'), nullable=False)
    mode = db.Column(db.Enum(Mode))
    group = relationship("GroupOrm", back_populates="users")
    user = relationship("UserOrm", back_populates="groups")
    __table_args__ = (db.UniqueConstraint('user_id', 'group_id', name='user_group'),)
