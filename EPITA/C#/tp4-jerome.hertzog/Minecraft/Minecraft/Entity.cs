using System;

namespace Minecraft
{
    #region dependencies
    public enum MobType
    {
        PLAYER,
        PIG,
        COW,
        OCELOT,
        ZOMBIE,
        CREEPER
    }
    #endregion

    public class Entity
    {
        //attributs
        protected MobType type;
        protected int hp;
        protected string noise;
        protected bool isKo;
        protected Blocks loot;
        
        //getters
        public MobType Type => type;
        public int HP
        {
            get => hp;
            set => hp = value;
        }

        public bool IsKo => isKo;
        
        #region Constructor
        public Entity(MobType type,int hp,string noise, Blocks loot)
        {
            this.type = type;
            this.hp = hp;
            this.noise = noise;
            this.loot = loot;
        }
        #endregion
        
        #region Methods

        public virtual void WhoAmI()
        {
            Console.WriteLine("I am an entity ! "+noise);
        }
        
        public virtual void Describe()
        {
            if (type == MobType.OCELOT)
                Console.WriteLine("I'm an "+type+" and I have "+hp+" hp");
            else
            {
                Console.WriteLine("I'm a "+type+" and I have "+hp+" hp");
            }
        }
        
        public Blocks GetHurt(int count)
        {
            hp -= count;
            if (hp <= 0)
            {
                isKo = true;
                hp = 0;
                return loot;
            }

            return null;
        }
        
        #endregion

    }
}