PGDMP          /                y           order_service_db    10.17    10.17                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3            ?            1259    16403    departments    TABLE     k   CREATE TABLE public.departments (
    department_id integer NOT NULL,
    department_name text NOT NULL
);
    DROP TABLE public.departments;
       public         postgres    false    3            ?            1259    16401    departments_department_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.departments_department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.departments_department_id_seq;
       public       postgres    false    3    197                       0    0    departments_department_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.departments_department_id_seq OWNED BY public.departments.department_id;
            public       postgres    false    196            ?            1259    16416 	   employees    TABLE     ?   CREATE TABLE public.employees (
    employee_id integer NOT NULL,
    fio text NOT NULL,
    "position" text NOT NULL,
    department_id integer NOT NULL
);
    DROP TABLE public.employees;
       public         postgres    false    3            ?            1259    16414    employees_employee_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.employees_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.employees_employee_id_seq;
       public       postgres    false    3    199                       0    0    employees_employee_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.employees_employee_id_seq OWNED BY public.employees.employee_id;
            public       postgres    false    198            ?            1259    16432    orders    TABLE       CREATE TABLE public.orders (
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
       public         postgres    false    3            ?            1259    16430    orders_order_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.orders_order_id_seq;
       public       postgres    false    3    201                       0    0    orders_order_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;
            public       postgres    false    200            }
           2604    16406    departments department_id    DEFAULT     ?   ALTER TABLE ONLY public.departments ALTER COLUMN department_id SET DEFAULT nextval('public.departments_department_id_seq'::regclass);
 H   ALTER TABLE public.departments ALTER COLUMN department_id DROP DEFAULT;
       public       postgres    false    197    196    197            ~
           2604    16419    employees employee_id    DEFAULT     ~   ALTER TABLE ONLY public.employees ALTER COLUMN employee_id SET DEFAULT nextval('public.employees_employee_id_seq'::regclass);
 D   ALTER TABLE public.employees ALTER COLUMN employee_id DROP DEFAULT;
       public       postgres    false    198    199    199            
           2604    16435    orders order_id    DEFAULT     r   ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);
 >   ALTER TABLE public.orders ALTER COLUMN order_id DROP DEFAULT;
       public       postgres    false    200    201    201                      0    16403    departments 
   TABLE DATA               E   COPY public.departments (department_id, department_name) FROM stdin;
    public       postgres    false    197                      0    16416 	   employees 
   TABLE DATA               P   COPY public.employees (employee_id, fio, "position", department_id) FROM stdin;
    public       postgres    false    199                      0    16432    orders 
   TABLE DATA               ~   COPY public.orders (order_id, created_dt, updated_dt, type_order, description, status, serial_number, creator_id) FROM stdin;
    public       postgres    false    201                       0    0    departments_department_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.departments_department_id_seq', 1, false);
            public       postgres    false    196                       0    0    employees_employee_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.employees_employee_id_seq', 1, false);
            public       postgres    false    198                       0    0    orders_order_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);
            public       postgres    false    200            ?
           2606    16413 +   departments departments_department_name_key 
   CONSTRAINT     q   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_department_name_key UNIQUE (department_name);
 U   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_department_name_key;
       public         postgres    false    197            ?
           2606    16411    departments departments_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (department_id);
 F   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_pkey;
       public         postgres    false    197            ?
           2606    16424    employees employees_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);
 B   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_pkey;
       public         postgres    false    199            ?
           2606    16440    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public         postgres    false    201            ?
           2606    16425 &   employees employees_department_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(department_id) ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_department_id_fkey;
       public       postgres    false    2691    197    199            ?
           2606    16441    orders orders_creator_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES public.employees(employee_id);
 G   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_creator_id_fkey;
       public       postgres    false    2693    201    199                  x?????? ? ?            x?????? ? ?            x?????? ? ?                     0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3            ?            1259    16403    departments    TABLE     k   CREATE TABLE public.departments (
    department_id integer NOT NULL,
    department_name text NOT NULL
);
    DROP TABLE public.departments;
       public         postgres    false    3            ?            1259    16401    departments_department_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.departments_department_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.departments_department_id_seq;
       public       postgres    false    3    197                       0    0    departments_department_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.departments_department_id_seq OWNED BY public.departments.department_id;
            public       postgres    false    196            ?            1259    16416 	   employees    TABLE     ?   CREATE TABLE public.employees (
    employee_id integer NOT NULL,
    fio text NOT NULL,
    "position" text NOT NULL,
    department_id integer NOT NULL
);
    DROP TABLE public.employees;
       public         postgres    false    3            ?            1259    16414    employees_employee_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.employees_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.employees_employee_id_seq;
       public       postgres    false    3    199                       0    0    employees_employee_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.employees_employee_id_seq OWNED BY public.employees.employee_id;
            public       postgres    false    198            ?            1259    16432    orders    TABLE       CREATE TABLE public.orders (
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
       public         postgres    false    3            ?            1259    16430    orders_order_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.orders_order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.orders_order_id_seq;
       public       postgres    false    3    201                       0    0    orders_order_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;
            public       postgres    false    200            }
           2604    16406    departments department_id    DEFAULT     ?   ALTER TABLE ONLY public.departments ALTER COLUMN department_id SET DEFAULT nextval('public.departments_department_id_seq'::regclass);
 H   ALTER TABLE public.departments ALTER COLUMN department_id DROP DEFAULT;
       public       postgres    false    197    196    197            ~
           2604    16419    employees employee_id    DEFAULT     ~   ALTER TABLE ONLY public.employees ALTER COLUMN employee_id SET DEFAULT nextval('public.employees_employee_id_seq'::regclass);
 D   ALTER TABLE public.employees ALTER COLUMN employee_id DROP DEFAULT;
       public       postgres    false    198    199    199            
           2604    16435    orders order_id    DEFAULT     r   ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);
 >   ALTER TABLE public.orders ALTER COLUMN order_id DROP DEFAULT;
       public       postgres    false    200    201    201                      0    16403    departments 
   TABLE DATA               E   COPY public.departments (department_id, department_name) FROM stdin;
    public       postgres    false    197   *                  0    16416 	   employees 
   TABLE DATA               P   COPY public.employees (employee_id, fio, "position", department_id) FROM stdin;
    public       postgres    false    199   G                  0    16432    orders 
   TABLE DATA               ~   COPY public.orders (order_id, created_dt, updated_dt, type_order, description, status, serial_number, creator_id) FROM stdin;
    public       postgres    false    201   d                   0    0    departments_department_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.departments_department_id_seq', 1, false);
            public       postgres    false    196                       0    0    employees_employee_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.employees_employee_id_seq', 1, false);
            public       postgres    false    198                       0    0    orders_order_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.orders_order_id_seq', 1, false);
            public       postgres    false    200            ?
           2606    16413 +   departments departments_department_name_key 
   CONSTRAINT     q   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_department_name_key UNIQUE (department_name);
 U   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_department_name_key;
       public         postgres    false    197            ?
           2606    16411    departments departments_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (department_id);
 F   ALTER TABLE ONLY public.departments DROP CONSTRAINT departments_pkey;
       public         postgres    false    197            ?
           2606    16424    employees employees_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);
 B   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_pkey;
       public         postgres    false    199            ?
           2606    16440    orders orders_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);
 <   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_pkey;
       public         postgres    false    201            ?
           2606    16425 &   employees employees_department_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_department_id_fkey FOREIGN KEY (department_id) REFERENCES public.departments(department_id) ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.employees DROP CONSTRAINT employees_department_id_fkey;
       public       postgres    false    2691    197    199            ?
           2606    16441    orders orders_creator_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_creator_id_fkey FOREIGN KEY (creator_id) REFERENCES public.employees(employee_id);
 G   ALTER TABLE ONLY public.orders DROP CONSTRAINT orders_creator_id_fkey;
       public       postgres    false    2693    201    199           