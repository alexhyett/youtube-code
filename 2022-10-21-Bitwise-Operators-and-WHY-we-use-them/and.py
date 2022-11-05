READ_PERMISSION = 4
WRITE_PERMISSION = 2
EXECUTE_PERMISSION = 1

userPermissions = 6

if (userPermissions & READ_PERMISSION) == READ_PERMISSION:
    print("Can Read")
else:
    print("Cannot Read")

print(userPermissions & READ_PERMISSION)
print(bin(userPermissions & READ_PERMISSION))
