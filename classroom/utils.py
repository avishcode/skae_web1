import uuid

def generate_classroom_id():
    get_classroom_id = str(uuid.uuid4()).replace('-', '').upper()[:10]
    return get_classroom_id

