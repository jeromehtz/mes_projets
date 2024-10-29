let build_line n str = match n with
  | n when n<0 -> failwith "build_line : n must be positive"
  | n ->
    let rec build_line_rec n = match n with
      | 0 -> ()
      | n ->
        print_string(str) ;
        build_line_rec(n-1)
    in build_line_rec n;;

let square n str =
  let rec square_rec n m str = match n with
    | 0 -> ()
    | n ->
      build_line m str ;
      print_newline() ;
      square_rec (n-1) m str
  in square_rec n n str;;

let square2 n (str1,str2) =
  let str = str1 ^ str2 in
  square n str ;;

let rec triangle n str = match n with
  | 0 -> ()
  | n ->
    triangle(n-1)(str) ;
    build_line n str ;
    print_newline() ;;

let pyramid n (str1,str2) =
  let m = n in
  let rec pyramid_rec n t = match (n,t) with
    | (0,t) when t>m -> ()
    | (n,t) when n=0 -> build_line(2*t)(str2) ; pyramid_rec 0 (t+1)
    | (n,t) ->
      build_line (n-1)(str1) ; build_line(2*t)(str2) ;
      build_line(n-1)(str1) ; print_newline() ;
      pyramid_rec(n-1)(t+1)
  in pyramid_rec n 1;;

let triangle_haut n (str1, str2) =
  let m = 2*n-1 in
  let rec triangle_1 a t = match (a,t) with
    | (a,t) when t=m-m/2 -> ()
    | (a,t) when a=0 -> build_line 1 str2 ; build_line (m-(a+1)*2) str1 ; build_line 1 str2 ; print_newline() ; triangle_1 (a+1) (t+1)
    | (a,t) -> build_line a str1 ; build_line 1 str2 ; build_line (m-(a+1)*2) str1 ; build_line 1 str2 ; 
      build_line a str1 ; print_newline() ; triangle_1 (a+1) (t+1)
  in triangle_1 0 1;;

let triangle_bas n (str1, str2) =
  let m = 2*n-1 in
  let rec triangle_2 a t = match (a,t) with
    | (0,t) when t=m/2 -> ()
    | (a,t) when a=0 && m>2 -> build_line 1 str2 ; build_line (m-2) str1 ; build_line 1 str2 ; print_newline() ; triangle_2 (0) (t+1)
    | (a,t) when t=1 && a=n-1 -> build_line a str1 ; build_line 1 str2 ; build_line a str1 ; print_newline() ; triangle_2 (a-1) (t-1)
    | (a,t) when m>a*2 -> build_line a str1 ; build_line 1 str2 ; build_line (m-(a+1)*2) str1 ; build_line 1 str2 ; 
                          build_line a str1 ; print_newline() ; triangle_2 (a-1) (t+1)
    | (a,t) -> invalid_arg "triangle_bas : invalid case"
  in triangle_2 (n-1) 1 ;;

let cross n (str1, str2) =
  triangle_haut n (str1, str2) ; triangle_bas n (str1, str2);;



