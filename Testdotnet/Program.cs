using Microsoft.EntityFrameworkCore;
using NSwag.AspNetCore;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<TestingDB>(opt => opt.UseInMemoryDatabase("testList"));
builder.Services.AddDatabaseDeveloperPageExceptionFilter();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddOpenApiDocument(config =>
{
    config.DocumentName = "TestingAPI";
    config.Title = "TestingAPI v1";
    config.Version = "v1";
});

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseOpenApi();
    app.UseSwaggerUi(config =>
    {
        config.DocumentTitle = "TestingAPI";
        config.Path = "/swagger";
        config.DocumentPath = "/swagger/{documentName}/swagger.json";
        config.DocExpansion = "list";
    });
}

app.MapGet("/", () => "Hello World!");

app.MapGet("/testitems", async (TestingDB db) =>
    await db.Test.Select(x => new TestItemDTO(x)).ToListAsync());

app.MapGet("/testitems/complete", async (TestingDB db) =>
    await db.Test.Where(t => t.IsComplete).Select(t => new TestItemDTO(t)).ToListAsync());

app.MapGet("/testitems/{id}", async (int id, TestingDB db) =>
    await db.Test.FindAsync(id)
        is Testing test
            ? Results.Ok(new TestItemDTO(test))
            : Results.NotFound());

app.MapPost("/testitems", async (Testing test, TestingDB db) =>
{
    var testItem = new Testing
    {
        IsComplete = test.IsComplete,
        Name = test.Name
    };
    db.Test.Add(test);
    await db.SaveChangesAsync();

    return Results.Created($"/testitems/{test.Id}", new TestItemDTO(test));
});

app.MapPut("/testitems/{id}", async (int id, Testing inputtest, TestingDB db) =>
{
    var test = await db.Test.FindAsync(id);

    if (test is null) return Results.NotFound();

    test.Name = inputtest.Name;
    test.IsComplete = inputtest.IsComplete;

    await db.SaveChangesAsync();

    return Results.NoContent();
});

app.MapDelete("/testitems/{id}", async (int id, TestingDB db) =>
{
    if (await db.Test.FindAsync(id) is Testing test)
    {
        db.Test.Remove(test);
        await db.SaveChangesAsync();
        return Results.NoContent();
    }

    return Results.NotFound();
});

app.Run();
