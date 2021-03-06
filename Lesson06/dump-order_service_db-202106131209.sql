PGDMP     8    	                y           order_service_db    10.17    10.17     
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3            ?            1259    16533    departments    TABLE     k   CREATE TABLE public.departments (
    department_id integer NOT NULL,
    department_name text NOT NULL
);
    DROP TABLE public.departments;
       public         postgres    false    3            ?            1259    16531    departments_department_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.departments_department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.departments_department_id_seq;
       public       postgres    false    201    3                       0    0    departments_department_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.departments_department_id_seq OWNED BY public.departments.department_id;
            public       postgres    false    200            ?            1259    16500 	   employees    TABLE     ?   CREATE TABLE public.employees (
    employee_id integer NOT NULL,
    fio text NOT NULL,
    "position" text NOT NULL,
    department_id integer NOT NULL
);
    DROP TABLE public.employees;
       public         postgres    false    3            ?            1259    16498    employees_employee_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.employees_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.employees_employee_id_seq;
       public       postgres    false    197    3                       0    0    employees_employee_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.employees_employee_id_seq OWNED BY public.employees.employee_id;
            public       postgres    false    196            ?            1259    16516    orders    TABLE       CREATE TABLE public.orders (
    order_id integer NOT NULL,
    created_dt date NOT NULL,
    updated_dt date NOT NULL,
    type_order text NOT NULL,
    description text NOT NULL,
    status text NOT NULL,
    serial_number integer NOT NULL,
    creator_id integer NOT NULL
);
    DROP TABLE public.orders;
       public         postgres    false    3            ?            1259    16514    orders_order_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.orders_order_id_seq;
       public       postgres    false    199    3                       0    0    orders_order_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;
            public       postgres    false    198            
           2604    16536    departments department_id    DEFAULT     ?   ALTER TABLE ONLY public.departments ALTER COLUMN department_id SET DEFAULT nextval('public.departments_department_id_seq'::regclass);
 H   ALTER TABLE public.departments ALTER COLUMN department_id DROP DEFAULT;
       public       postgres    false    201    200    201            }
           2604    16503    employees employee_id    DEFAULT     ~   ALTER TABLE ONLY public.employees ALTER COLUMN employee_id SET DEFAULT nextval('public.employees_employee_id_seq'::regclass);
 D   ALTER TABLE public.employees ALTER COLUMN employee_id DROP DEFAULT;
       public       postgres    false    196    197    197            ~
           2604    16519    orders order_id    DEFAULT     r   ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);
 >   ALTER TABLE public.orders ALTER COLUMN order_id DROP DEFAULT;
       public       postgres    false    199    198    199                      0    16533    departments 
   TABLE DATA               E   COPY public.departments (department_id, department_name) FROM stdin;
    public       postgres    false    201                      0    16500 	   employees 
   TABLE DATA               P   COPY public.employees (employee_id, fio, "position", department_id) FROM stdin;
    public       postgres    false    197                      0    16516    orders 
   TABLE DATA               ~   COPY public.orders (order_id, created_dt, updated_dt, type_order, description, status, serial_number, creator_id) FROM stdin;
    public       postgres    false    199                       0    0    departments_department_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.departments_department_id_seq', 4, true);
            public       postgres    false    200                       0    0    employees_employee_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.employees_employee_id_seq', 10, true);
            public       postgres    false    196                       0    0    orders_order_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.orders_order_id_seq', 12, true);
            public       postgres    false    198            ?
           2606    16543 +   departments departments_department_name_key 
   CONSTRAINT     q   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_department_name_key UNIQUE (department_name);
 U   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_department_name_key;
       public         postgres    false    201            ?
           2606    16541    departments departments_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (department_id);
 F   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_pkey;
       public         postgres    false    201            ?
           2606    16508    employees employees_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);
 B   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_pkey;
       public         postgres    false    197            ?
           2606    16524    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public         postgres    false    199            ?
           2606    16525    orders orders_creator_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES public.employees(employee_id);
 G   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_creator_id_fkey;
       public       postgres    false    2689    199    197               c   x???	?0D??*? ????H??V???ළَ\Üf??r?A??????	?`???`?N<V0Nq	E?4?y!?֡???O?2???2VSm???'@?         E  x?m?]NA??gN?'0???]<̺D4?DT?!!}?w??^??FV????&??_wUM?a?	?Xa??E??E)W:????????c?ȱ?4?#??$???8????\???ݔee!?Ar?????#??b???n7}??͐??&??%?W
?(???<???|?YwDI&h.?:??A???c?Jߴ???k??H?`#??RG,?2Ac?SK=?-w????qnc?t65?m??ĭ3??mj????4??k?O?G?Gn?
????G?8???``?)^????g5G{??n?a?YE??pn?J}???R?H??^G????x? ???+         ?   x?m?[
?0E?gV?*y4??şJ)HRK?U?@??%9	j?&?%????bi?1L???L?X=g??%ʕ?????W@A???IB讚????J???F?.^??i	5r?dd?R????t??m{gu?jP?_?M?Rl?<??&??_XC9????Z??z??R??i???}X?          
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3            ?            1259    16533    departments    TABLE     k   CREATE TABLE public.departments (
    department_id integer NOT NULL,
    department_name text NOT NULL
);
    DROP TABLE public.departments;
       public         postgres    false    3            ?            1259    16531    departments_department_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.departments_department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.departments_department_id_seq;
       public       postgres    false    201    3                       0    0    departments_department_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.departments_department_id_seq OWNED BY public.departments.department_id;
            public       postgres    false    200            ?            1259    16500 	   employees    TABLE     ?   CREATE TABLE public.employees (
    employee_id integer NOT NULL,
    fio text NOT NULL,
    "position" text NOT NULL,
    department_id integer NOT NULL
);
    DROP TABLE public.employees;
       public         postgres    false    3            ?            1259    16498    employees_employee_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.employees_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.employees_employee_id_seq;
       public       postgres    false    197    3                       0    0    employees_employee_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.employees_employee_id_seq OWNED BY public.employees.employee_id;
            public       postgres    false    196            ?            1259    16516    orders    TABLE       CREATE TABLE public.orders (
    order_id integer NOT NULL,
    created_dt date NOT NULL,
    updated_dt date NOT NULL,
    type_order text NOT NULL,
    description text NOT NULL,
    status text NOT NULL,
    serial_number integer NOT NULL,
    creator_id integer NOT NULL
);
    DROP TABLE public.orders;
       public         postgres    false    3            ?            1259    16514    orders_order_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.orders_order_id_seq;
       public       postgres    false    199    3                       0    0    orders_order_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;
            public       postgres    false    198            
           2604    16536    departments department_id    DEFAULT     ?   ALTER TABLE ONLY public.departments ALTER COLUMN department_id SET DEFAULT nextval('public.departments_department_id_seq'::regclass);
 H   ALTER TABLE public.departments ALTER COLUMN department_id DROP DEFAULT;
       public       postgres    false    201    200    201            }
           2604    16503    employees employee_id    DEFAULT     ~   ALTER TABLE ONLY public.employees ALTER COLUMN employee_id SET DEFAULT nextval('public.employees_employee_id_seq'::regclass);
 D   ALTER TABLE public.employees ALTER COLUMN employee_id DROP DEFAULT;
       public       postgres    false    196    197    197            ~
           2604    16519    orders order_id    DEFAULT     r   ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);
 >   ALTER TABLE public.orders ALTER COLUMN order_id DROP DEFAULT;
       public       postgres    false    199    198    199                      0    16533    departments 
   TABLE DATA               E   COPY public.departments (department_id, department_name) FROM stdin;
    public       postgres    false    201   o                 0    16500 	   employees 
   TABLE DATA               P   COPY public.employees (employee_id, fio, "position", department_id) FROM stdin;
    public       postgres    false    197   ?                 0    16516    orders 
   TABLE DATA               ~   COPY public.orders (order_id, created_dt, updated_dt, type_order, description, status, serial_number, creator_id) FROM stdin;
    public       postgres    false    199   7                   0    0    departments_department_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.departments_department_id_seq', 4, true);
            public       postgres    false    200                       0    0    employees_employee_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.employees_employee_id_seq', 10, true);
            public       postgres    false    196                       0    0    orders_order_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.orders_order_id_seq', 12, true);
            public       postgres    false    198            ?
           2606    16543 +   departments departments_department_name_key 
   CONSTRAINT     q   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_department_name_key UNIQUE (department_name);
 U   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_department_name_key;
       public         postgres    false    201            ?
           2606    16541    departments departments_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (department_id);
 F   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_pkey;
       public         postgres    false    201            ?
           2606    16508    employees employees_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);
 B   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_pkey;
       public         postgres    false    197            ?
           2606    16524    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public         postgres    false    199            ?
           2606    16525    orders orders_creator_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES public.employees(employee_id);
 G   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_creator_id_fkey;
       public       postgres    false    2689    199    197           