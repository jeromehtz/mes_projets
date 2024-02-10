using System;

namespace Minecraft
{
    public class Aggressive : Entity
    {
        private int strength;
        # region Constructor

        public Aggressive(MobType type, int hp, string noise, Blocks loot,
            int strength) : base (type, hp, noise, loot)
        {
            this.strength = strength;
        }
        
        #endregion
        
        #region Methods
        
        public override void WhoAmI()
        {
            Console.WriteLine("I'm aggressive ! "+noise);
        }
        
        public void Attack(Entity entity)
        {
            entity.HP -= strength;
            if (entity.HP <= 0)
            {
                entity.HP = 0;
            }
        }

        #endregion
    }
}