class feishu_data:
    def __int__(self):
        self.create_table_channel = "create table translate_channel(channel_id int primary key auto_increment," \
                                    "channel varchar(25))"
        self.create_table_data = "create table translate_statistics(execute_id int primary key auto_increment," \
                                 "channel_id int,newly_quantity int, modify_quantity int," \
                                 " quantity int,time TIMESTAMP default current_timestamp," \
                                 "foreign key (channel_id) references translate_channel(channel_id))"

        self.insert_table_channel = "INSERT INTO translate_channel (channel_id,channel) VALUES ( 3,'server'),(4,'unity')"
        self.insert_execute_statistics = "insert into translate_statistics (channel_id,newly_quantity,modify_quantity,quantity) " \
                                         "values (1,51,200,980)"
