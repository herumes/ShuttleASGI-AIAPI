import uuid
import random
import string

def gen_uuid() -> str:
   """Generate a UUID."""
   return str(uuid.uuid4())

def gen_random_string(prefix: str, length: int = 29, charset: str = string.ascii_letters + string.digits) -> str:
   """Generate a random string with a given prefix and length."""
   return prefix + ''.join(random.choices(charset, k=length))

def gen_cmpl_id() -> str:
   """Generate a chat completion ID."""
   return gen_random_string('chatcmpl-')

def gen_sys_fp(k: int = 10) -> str:
   """Generate a system fingerprint."""
   return gen_random_string('fp_', length=k, charset=string.ascii_lowercase + string.digits)

def gen_req_id() -> str:
   """Generate a request ID."""
   return gen_random_string('req_')