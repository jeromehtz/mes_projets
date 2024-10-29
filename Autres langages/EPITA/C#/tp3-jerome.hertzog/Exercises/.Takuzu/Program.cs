namespace Takuzu
{
    class Program
    {
        static void Main(string[] args)
        {
            Takuzu.Game(new int[4,4]
            {
                {
                    -1, 1, -1, 0
                },
                {
                    -1, -1, 0, -1
                },
                {
                    -1, 0, -1, -1
                },
                {
                    1, 1, -1, 0
                }
            });
        }
    }
}