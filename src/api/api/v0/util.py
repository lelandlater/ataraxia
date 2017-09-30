def _generate_id(num_bytes=16):
    return base64.b64encode(m2Crypto.m2.rand_bytes(num_bytes))

def _authorize_jwt(token):
    # ...
    return None