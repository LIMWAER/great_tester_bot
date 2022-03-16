DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS log;
CREATE TABLE users
(
    chat_id   bigint not null,
    username  text,
    full_name text
);

CREATE TABLE log
(
    log_id  serial not null,
    chat_id bigint not null,
    info    text,
    date    time
);
ALTER TABLE users
    ADD
        CONSTRAINT PK_users PRIMARY KEY
            (
             chat_id
                )
;
ALTER TABLE log
    ADD
        CONSTRAINT PK_log PRIMARY KEY
            (
             log_id
                )
;
ALTER TABLE log
    ADD
        CONSTRAINT FK_log_users FOREIGN KEY
            (
             chat_id
                ) REFERENCES users (
                                    chat_id
                )
;
ALTER TABLE users
    owner TO postgres;
ALTER TABLE log
    owner TO postgres;

CREATE
UNIQUE index users_id_uindex ON users (chat_id);