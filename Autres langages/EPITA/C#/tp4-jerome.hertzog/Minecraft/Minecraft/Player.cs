using System;
using System.Collections.Generic;

namespace Minecraft
{
    public class Player : Entity
    {
        //attributs 
        private int weaponStrength;
        private string username;
        private List<Blocks> inventory;
        # region Constructor
        public Player(string username, int weaponStrength)
            : base(MobType.PLAYER, 20, "Hi Guys", new Blocks(Blocks.BlockType.NONE,0))
        {
            this.username = username;
            this.weaponStrength = weaponStrength;
            inventory = new List<Blocks>();
        }
        #endregion

        #region Methods
        
        public override void WhoAmI()
        {
            Console.WriteLine("I am "+username+" ! "+noise);
        }
        
        public void Attack(Entity entity)
        {
            entity.HP -= weaponStrength + 1;
            inventory.Add(GetHurt(weaponStrength + 1));
        }
        
        public void AddInInventory(Blocks blocks)
        {
            int i = inventory.Count;
            Console.WriteLine("longueur : "+inventory.Count);
            while (i<64 && blocks.count!=0)
            {
                inventory.Add(blocks);
                i += 1;
            }
            Console.WriteLine("Nouvelle longueur : "+inventory.Count);
        }
        
        public void RemoveInInventory(Blocks blocks)
        {
            int i = 0;
            while (i<inventory.Count && blocks.count!=0)
            {
                if (inventory[i].type == blocks.type)
                {
                    inventory.RemoveAt(i);
                    blocks.count -= 1;
                }

                i += 1;
            }
        }
        
        public void Heal(int life)
        {
            Console.WriteLine(hp);
            if (hp > 0)
            {
                //life = hp - life;
                Console.WriteLine(life);
                hp += life;
            }
            Console.WriteLine(hp);
        }
        
        public void DisplayInventory()
        {
            foreach (Blocks element in inventory)
            {
                Console.Write(element+" | ");
            }
        }
        
        public int CountInInventory(Blocks.BlockType type)
        {
            int counter = 0;
            Console.WriteLine(inventory.Count);
            for (int i=0; i<inventory.Count-1; i++)
            {
                Console.WriteLine((i,inventory[i].type));
                if (inventory[i].type == type)
                {
                    counter += 1;
                }
            }

            return counter;
        }

        #endregion
    }
}