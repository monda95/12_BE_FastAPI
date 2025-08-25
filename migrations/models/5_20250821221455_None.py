from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `meetings` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `url_code` VARCHAR(255) NOT NULL UNIQUE,
    `title` VARCHAR(255) NOT NULL DEFAULT '',
    `location` VARCHAR(255) NOT NULL DEFAULT '',
    `start_date` DATE,
    `end_date` DATE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `participants` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `name` VARCHAR(255) NOT NULL,
    `meeting_id` VARCHAR(255) NOT NULL,
    KEY `idx_participant_meeting_1de158` (`meeting_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `participant_date` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `created_at` DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    `date` DATE NOT NULL,
    `enabled` BOOL NOT NULL DEFAULT 1,
    `starred` BOOL NOT NULL DEFAULT 0,
    `participant_id` BIGINT NOT NULL,
    KEY `idx_participant_partici_e7f9bd` (`participant_id`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
