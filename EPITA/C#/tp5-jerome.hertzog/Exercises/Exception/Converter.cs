using System;

namespace Exception
{
    public class Converter
    {
        public static double DegToRad(double angle)
        {
            double angle_Pi = 180 / angle;
            angle = Math.PI / angle_Pi;
            double Pi = Math.PI;
            if (angle < -Pi || angle > Pi)
                throw new ArgumentException("angle invalide");
            return angle;

        }

        public static double RadToDeg(double angle)
        {
            double Pi = Math.PI;
            if (angle < -Pi || angle > Pi)
                throw new ArgumentException("angle invalide"); 
            double Pi_angle = Pi / angle;
            return 180 / Pi_angle;
        }
    }
}