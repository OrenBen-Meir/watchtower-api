-- for development on a windows machine, to be used for a localdb, not needed for linux and mac users because docker is used
CREATE LOGIN myuser WITH PASSWORD = 'Password123'
GO
CREATE USER myuser FOR LOGIN myuser
GO
EXEC sp_addrolemember 'db_owner', 'myuser'
GO
