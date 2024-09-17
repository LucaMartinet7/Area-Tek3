public class TestItemDTO
{
    public int Id { get; set; }
    public string? Name { get; set; }
    public bool IsComplete { get; set; }

    public TestItemDTO() { }
    public TestItemDTO(Testing TestItem) =>
    (Id, Name, IsComplete) = (TestItem.Id, TestItem.Name, TestItem.IsComplete);
}