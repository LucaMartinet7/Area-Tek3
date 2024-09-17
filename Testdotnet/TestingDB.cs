using Microsoft.EntityFrameworkCore;

class TestingDB : DbContext
{
    public TestingDB(DbContextOptions<TestingDB> options)
        : base(options) { }

    public DbSet<Testing> Test => Set<Testing>();
}