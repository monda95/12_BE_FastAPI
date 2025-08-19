from tortoise import fields


class BaseModel:
    id = fields.BigIntField(pk=True)
    create_at = fields.DatetimeField(auto_now_add=True)


# MySQL : primary key 를 정할 때 주의해야 하는 점
# 8버전 이상이라면 innodb 가 default engine이다 (옛날 MyISAM)

# innodb 의 특징 중 하나는 -> clustering index
# primary key 를 기준으로 값이 비슷한 row들끼리 disk에서도 실제로 모여있음

# HDD
# 랜덤 IO가 느리고 , 순차 IO가 빠름.

# BigInt가 느릴텐데 쓰는 이유 => 유저가 생성하는 테이블은 INT의 한계가 21억
# 그 이상일 땐 오버플로우x 인서트 자체가 안 됨. 따라서 맘 편하게 BigInt
