import uuid

def generate():
    """Generate Random ID"""
    return str(uuid.uuid4().hex)
