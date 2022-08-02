-- Active: 1658998083382@@127.0.0.1@3306@project_db
use project_db;


# 노인 만성질병 의사진단 기준
select * from disease_doctor;

# 연도별 의사진단 질병 수
select 만성질환수별,소계 from disease_doctor
WHERE 시점 = 2014;

select 만성질환수별,소계 from disease_doctor
WHERE 시점 = 2017;

select 만성질환수별,소계 from disease_doctor
WHERE 시점 = 2020;

# 연도별, 분위별 의사진단 질병 수
select 만성질환수별,소계,제1오분위,제2오분위,제3오분위,제4오분위,제5오분위
 from disease_doctor
 WHERE 시점 = 2020;

 # 노인 만성질병 본인인지 기준
 select * from disease_self;

 # 만성질병 종류별
 select * from disease_sort;

# 수진율 및 미치료율
select * from treat_rate;

# 요양 시설
select * from facility;

# 노인 우울 증상
select * from blues;



# 연도별 의사진단 질병 수
select 시점,만성질환수별,소계 from disease_doctor
WHERE 만성질환수별 in ('없음 (%)','1개 (%)','2개 (%)','3개 이상 (%)') 
order by 시점;

-- select * from disease_doctor
-- UNION ALL
-- select * from disease_self;

select * from disease_sort
where 항목='유병률 (%)' and 성별='전체';

select * from disease_sort;

drop table disease_sort2;
create table disease_sort2
        (disease VARCHAR(30),
        2014년 FLOAT,
         2017년 FLOAT,
         2020년 FLOAT);


select * from disease_sort2
order by 2020년 desc
limit 10;


