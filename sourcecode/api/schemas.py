from run import ma

class UserSchema(ma.Schema):
    uid=fields.Int()
    suri=fields.Str()
    name=fields.Str()
    active=fields.Bool()
    hosting=fields.Bool()
    evid=fields.Int()

class EventSchema(Schema):
    evid=fields.Int()
    host=fields.Str()
    pin=fields.Int()

class CueSchema(Schema):
    cid=fields.Int()
    playing=fields.Str()
    next=fields.Str()
    seed=fields.Str()

class TrackSchema(Schema):
    tid=fields.Int()
    cue=fields.Int()
    index=fields.Float()
    
class ResponseSchema(Schema):
    code=fields.Int()
    message=fields.Str()
    