READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXECUTE_PERMISSION = 1

userPermissions = READ_PERMISSION | WRITE_PERMISSION

userPermissions |= EXECUTE_PERMISSION

print(userPermissions)
print(bin(userPermissions))