(* MAISON 
#load "graphics.cma" ;;
*)

(* EPITA
# use "topfind" ;;
# require "graphics" ;;
*)
open Graphics ;;
open_graph " 1200x800 " ;;

let draw_line (x,y) (z,t) =
  moveto x y ;
  lineto z t ;;

(* MOUNTAIN *)
let rec mountain n (x,y) (z,t) = match n with
    0 -> draw_line (x,y) (z,t)
  | n -> let m = (x + z)/2 and h = (y+t)/2 + Random.int((abs(z-x)/3)+10*n) in
             mountain(n-1)(x,y)(m,h) ; mountain(n-1)(m,h)(z,t) ;;

(* DRAGON *)
let rec dragon n (x,y)(z,t) = match n with
    0 -> draw_line (x,y) (z,t)
  | n -> 
    dragon (n-1) (x,y) ((x+z)/2+(t-y)/2, (y+t)/2-(z-x)/2) ;
    dragon (n-1) (z,t) ((x+z)/2+(t-y)/2, (y+t)/2-(z-x)/2) ;;

(* TAPIS DE SIERPINSKI *)
let carpet n (x,y) = 
  clear_graph() ;
  let rec carpet_rec n (x,y) = match n with 
      n when n < 3 -> fill_rect x y n n 
    | _ -> (
              let m = n/3 in 
              carpet_rec(m)(x,y);
              carpet_rec(m)(x + m,y);
              carpet_rec(m)(x + 2*m,y); 
              carpet_rec(m)(x,y + m);
              carpet_rec(m)(x + 2*m, y + m); 
              carpet_rec(m)(x,y + 2*m);
              carpet_rec(m)(x + m, y + 2*m);
              carpet_rec(m)(x + 2*m, y + 2*m)
            ) 
  in carpet_rec(n)(x,y);;

(* TRIANGLE DE SIERPINSKI *)
let triangle(x1,y1) size =
  moveto x1 y1 ;
  lineto (x1+size/2)(y1+size-size/6) ;
  moveto x1 y1 ;
  lineto (x1+size)(y1);
  moveto (x1+size)(y1);
  lineto (x1+size/2)(y1+size-size/6) ;;

let rec sierpinski n (x,y) size = match n with
  | 0 -> triangle (x,y) size
  | _ -> sierpinski(n-1) (x,y) (size/2) ; 
    sierpinski(n-1)(x+size/2,y) (size/2) ; 
    sierpinski(n-1)(x+size/4,y+(5*size)/12) (size/2);;

(* CIRCLES *)
let color i = match i with 
  | i when i mod 2 = 0 -> set_color red
  | i -> set_color blue ;;

let four_circles r (x,y) limit = 
  let rec four_circles i r (x,y) limit = match r with
    | r when r<limit -> ()
    | r -> 
      color i ;
      draw_circle x y r ; 
      four_circles (i+1) (r/2) (x,y) limit ;
      four_circles (i+1) (r/2) (x,y+r/2) limit ;
      four_circles (i+1) (r/2) (x+r/2,y) limit ;
      four_circles (i+1) (r/2) (x,y-r/2) limit ;
      four_circles (i+1) (r/2) (x-r/2,y) limit 
  in four_circles 0 r (x,y) limit ;;


(* VICSEK (non terminee) *)
let carres x y size =
  fill_rect x y size size ;
  fill_rect (x+size) (y+size) size size ;
  fill_rect (x+size) (y-size) size size ;
  fill_rect (x-size) (y+size) size size ;
  fill_rect (x-size) (y-size) size size ;;

let rec vicsek_star n (x,y) size = match n with
  | 0 -> carres x y size
  | n -> 
    vicsek_star (n-1) (x,y) (size/2);
    vicsek_star (n-1) (x+size+size/2,y+size+size/2) (size/2);;            

(* FLECHE *)

let rec arrow r (x,y) o limit = match o with
  | o when o = 'N' -> let rec arrow1 n r (x,y) = match (r,n) with
    | (r,_) when r<limit -> ()
    | (r,n) when n = 1 -> fill_circle x y r ;
      arrow1 (n+1)(r/2)(x+(3*r)/2,y)  ;
      arrow1 (n+1)(r/2)(x,y+(3*r)/2) ;
      arrow1 (n+1)(r/2)(x-(3*r)/2,y)
    | (r,_) -> fill_circle x y r ;
      arrow1 (n+1)(r/2)(x+(3*r)/2,y) ;
      arrow1 (n+1)(r/2)(x,y+(3*r)/2) ;
      arrow1 (n+1)(r/2)(x-(3*r)/2,y) ;
      arrow1 (n+1)(r/2)(x,y-(3*r)/2)
    in arrow1 1 r (x,y)
  | o when o = 'S' -> let rec arrow2 n r (x,y) = match (r,n) with
    | (r,_) when r<limit -> ()
    | (r,n) when n = 1 -> fill_circle x y r ;
      arrow2 (n+1)(r/2)(x+(3*r)/2,y) ;
      arrow2 (n+1)(r/2)(x,y-(3*r)/2) ;
      arrow2 (n+1)(r/2)(x-(3*r)/2,y)
    | (r,_) -> fill_circle x y r ;
      arrow2 (n+1)(r/2)(x+(3*r)/2,y) ;
      arrow2 (n+1)(r/2)(x,y+(3*r)/2) ;
      arrow2 (n+1)(r/2)(x-(3*r)/2,y) ;
      arrow2 (n+1)(r/2)(x,y-(3*r)/2)
    in arrow2 1 r (x,y)
  | o when o = 'E' -> let rec arrow3 n r (x,y) = match (r,n) with
    | (r,_) when r<limit -> ()
    | (r,n) when n = 1 -> fill_circle x y r ;
      arrow3 (n+1)(r/2)(x+(3*r)/2,y) ;
      arrow3 (n+1)(r/2)(x,y+(3*r)/2) ;
      arrow3 (n+1)(r/2)(x,y-(3*r)/2)
    | (r,_) -> fill_circle x y r ;
      arrow3 (n+1)(r/2)(x+(3*r)/2,y) ;
      arrow3 (n+1)(r/2)(x,y+(3*r)/2) ;
      arrow3 (n+1)(r/2)(x-(3*r)/2,y) ;
      arrow3 (n+1)(r/2)(x,y-(3*r)/2)
    in arrow3 1 r (x,y)
  | o when o = 'O' -> let rec arrow4 n r (x,y) = match (r,n) with
    | (r,_) when r<limit -> ()
    | (r,n) when n = 1 -> fill_circle x y r ;
      arrow4 (n+1)(r/2)(x,y+(3*r)/2) ;
      arrow4 (n+1)(r/2)(x-(3*r)/2,y) ;
      arrow4 (n+1)(r/2)(x,y-(3*r)/2)
    | (r,_) -> fill_circle x y r ;
      arrow4 (n+1)(r/2)(x+(3*r)/2,y) ;
      arrow4 (n+1)(r/2)(x,y+(3*r)/2) ;
      arrow4 (n+1)(r/2)(x-(3*r)/2,y) ;
      arrow4 (n+1)(r/2)(x,y-(3*r)/2)
    in arrow4 1 r (x,y)
  | _ -> invalid_arg "arrow : o is not valid" ;;






