from repository_sqlite import Repository

test_repo = Repository('test.db')
test_repo.drop_db()
test_repo.__create_db__()

test_repo.save_uom("test_uom_1", "first test unit of measure")
test_repo.save_uom("test_uom_2", "second test unit of measure")
for row in test_repo.retrieve_uoms():
    print(row["id"])

print(test_repo.retrieve_uom_by_name("test_uom_1")["description"])

test_repo.drop_db()


