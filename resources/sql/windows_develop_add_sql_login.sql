CREATE LOGIN myuser WITH PASSWORD = 'Password123'
GO
CREATE USER myuser FOR LOGIN myuser
GO
EXEC sp_addrolemember 'db_owner', 'myuser'
GO
