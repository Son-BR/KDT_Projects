-- Active: 1658998083382@@127.0.0.1@3306@project_db
use project_db;

select 시점,만성질환수별,소계 from disease_doctor
WHERE 만성질환수별 in ('없음 (%)','1개 (%)','2개 (%)','3개 이상 (%)')
 order by 시점;

select disease, 유병률2020, 치료율2020 from disease_sort2
order by 유병률2020 desc
limit 10;

select * from disease_sort
where 항목 in ('유병률 (%)','치료율 (%)') and 성별='전체';

select disease, 치료율2020 from disease_sort2
order by 치료율2020
limit 10;

select 시점,소계 from blues
where 증상별 = '우울증상 (%)';

select 시점, (노인요양시설+노인요양공동생활가정) as 시설수
from facility
WHERE 항목='시설수 (개소)';

select 시점, (노인요양시설+노인요양공동생활가정) as 입소정원
from facility
WHERE 항목='입소정원 (명)';

select 수진율및미치료율별,과목별,소계 from treat_rate
where 과목별 in ('건강검진','치매검진','병의원 진료','치과 진료') and 시점='2020';


select 수진율및미치료율별,과목별,제1오분위,제2오분위,제3오분위,제4오분위,제5오분위
from treat_rate
where 과목별 = '건강검진' and 시점='2020';

select 제1오분위,제2오분위,제3오분위,제4오분위,제5오분위 from disease_doctor
WHERE 만성질환수별 = '없음 (%)' and 시점 = '2020';

select 제1오분위,제2오분위,제3오분위,제4오분위,제5오분위 from disease_doctor
WHERE 만성질환수별 = '3개 이상 (%)' and 시점 = '2020';

select 제1오분위,제2오분위,제3오분위,제4오분위,제5오분위 from blues
where 증상별='우울증상 (%)' and 시점 = '2020';
