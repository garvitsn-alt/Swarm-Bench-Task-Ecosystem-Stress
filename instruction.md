Working directory:
/workspace

Ecosystem Stress Benchmark

You are given a folder of environmental PDF reports.

Your task is to:

1. Read all reports
2. Extract environmental evidence
3. Calculate:
   - water_domain_score
   - soil_domain_score
   - forest_domain_score
   - mixed_domain_score
   - retrieval_score
4. Calculate final_synthesis_value

Write the final answer to:

/logs/agent/output.json

Return JSON only.

---

# Input Files

The reports are located at:

/environment/input_artifacts/

Use all reports. Do not ignore files.

---

# Output Format

The output must be valid JSON with exactly this structure:

{
  "source_files_used": [],
  "water_domain_score": 0,
  "soil_domain_score": 0,
  "forest_domain_score": 0,
  "mixed_domain_score": 0,
  "retrieval_score": 0,
  "final_synthesis_value": 0
}


source_files_used must list every PDF file used from /environment/input_artifacts/.

Use exact filenames including .pdf.


---

# General Rules

- flags must be 0 or 1
- severity_class must be from 1 to 5
- affected_scale must be from 1 to 4
- impact_scale must be from 1 to 4


Use evidence from report text.

Do not use:
- PDF viewer page number
- physical page count
- page index

---


Extract:

- contaminant_count
- human_health_flag
- aquatic_ecosystem_flag
- industrial_source_flag
- fire_risk_flag
- conservation_gap_flag
- monitoring_only_flag
- impact_scale
- air_pollution_flag
- mining_impact_flag
- industrial_pollution_flag
- multi_system_damage_flag
- ecological_damage_flag
- conceptual_flag
- severity_class
- mine_water_rebound_page
- dying_of_happiness_page
- remediation_flag
- severity_class
- erosion_flag
- salinity_flag
- fertility_loss_flag
- desertification_flag
- pollution_flag
- restoration_flag
- affected_scale
- forest_loss_flag
- habitat_loss_flag
- biodiversity_decline_flag
- upload_prefire_alert_page
- acid_mine_drainage_page
- falling_out_with_hal_page
- fire_prone_areas_page
- prediction_control_acid_page
- afterword_page
- comparison_prefire_page


Definitions:

human_health_flag:
1 if direct human health or drinking water risk is discussed

aquatic_ecosystem_flag:
1 if aquatic ecosystems or marine systems are affected

industrial_source_flag:
1 if industrial, mining, sewage, or waste discharge sources are discussed

remediation_flag:
1 if treatment, cleanup, restoration, or mitigation is discussed

erosion_flag:
1 if direct soil erosion or topsoil loss is discussed

salinity_flag:
1 if salinity or salt-related degradation is discussed

fertility_loss_flag:
1 if nutrient decline or soil fertility decline is discussed

desertification_flag:
1 if desertification or dryland degradation is discussed

pollution_flag:
1 if direct soil contamination or pollutants are discussed

restoration_flag:
1 if restoration or rehabilitation is discussed

forest_loss_flag:
1 if direct forest decline or fragmentation is discussed

habitat_loss_flag:
1 if habitat destruction or fragmentation is discussed

biodiversity_decline_flag:
1 if biodiversity decline or species loss is discussed

fire_risk_flag:
1 if forest fire or fire-risk evidence is discussed

conservation_gap_flag:
1 if conservation weakness or evidence gaps are discussed

monitoring_only_flag:
1 if the report is mainly monitoring or assessment focused

air_pollution_flag:
1 if atmospheric pollution or emissions are discussed

mining_impact_flag:
1 if mining-related environmental damage is discussed

industrial_pollution_flag:
1 if industrial contamination or discharge is discussed

multi_system_damage_flag:
1 if multiple environmental systems are affected

ecological_damage_flag:
1 if direct environmental or ecological harm is discussed

conceptual_flag:
1 if the report is mostly conceptual or non-evidence focused



Rules:

severity_class:
1=low
2=moderate
3=serious
4=severe
5=extreme

Calculate:

 
affected_scale:
1=local
2=regional
3=national
4=global
 

 
impact_scale:
1=local
2=regional
3=national
4=global

 

severity_class:
1=low
2=moderate
3=serious
4=severe
5=extreme

 contaminant_count:
      - 0 = no contaminant groups discussed
      - 1 = 1-2 contaminant groups discussed
      - 2 = 3-4 contaminant groups discussed
      - 3 = 5 or more contaminant groups discussed




Use printed book/report page numbers from the table of contents.
Do not use:
- PDF viewer page number
- physical page count
- page index



Calculate:


water_raw_score =
contaminant_count * 6
+ human_health_flag * 15
+ aquatic_ecosystem_flag * 12
+ industrial_source_flag * 10
+ severity_class * 8
- remediation_flag * 5

if contaminant_count > 4:
water_raw_score = water_raw_score + 7

if human_health_flag = 1 and aquatic_ecosystem_flag = 1:
water_raw_score = water_raw_score + 8

if remediation_flag = 1 and severity_class < 3:
water_raw_score = water_raw_score - 6

water_domain_score =
average(all water_raw_score)

if water_domain_score > 82:
water_domain_score = water_domain_score + 5


soil_raw_score =
erosion_flag * 12
+ salinity_flag * 10
+ fertility_loss_flag * 14
+ desertification_flag * 18
+ pollution_flag * 13
+ affected_scale * 10
- restoration_flag * 6

if desertification_flag = 1 and affected_scale > 2:
soil_raw_score = soil_raw_score * 1.15

if erosion_flag = 1 and fertility_loss_flag = 1:
soil_raw_score = soil_raw_score + 7

if restoration_flag = 1 and pollution_flag = 0:
soil_raw_score = soil_raw_score - 5

soil_domain_score =
average(all soil_raw_score)

if soil_domain_score > 80:
soil_domain_score = soil_domain_score + 4

 


forest_raw_score =
forest_loss_flag * 16
+ habitat_loss_flag * 14
+ biodiversity_decline_flag * 16
+ fire_risk_flag * 10
+ conservation_gap_flag * 8
+ impact_scale * 10
- monitoring_only_flag * 10

if forest_loss_flag = 1 and biodiversity_decline_flag = 1:
forest_raw_score = forest_raw_score + 10

if fire_risk_flag = 1 and impact_scale > 2:
forest_raw_score = forest_raw_score + 6

if monitoring_only_flag = 1 and forest_raw_score > 45:
forest_raw_score = 45

forest_domain_score =
average(all forest_raw_score)

if forest_domain_score > 78:
forest_domain_score = forest_domain_score + 6

 



value_1 =
(dying_of_happiness_page + upload_prefire_alert_page)
- mine_water_rebound_page

value_2 =
(acid_mine_drainage_page + fire_prone_areas_page)
- falling_out_with_hal_page

value_3 =
(prediction_control_acid_page + afterword_page)
- comparison_prefire_page

retrieval_score =
round(
(
abs(value_1)
+ floor(value_2 / 10)
+ floor(value_3 / 10)
) / 5
)


mixed_raw_score =
air_pollution_flag * 10
+ mining_impact_flag * 14
+ industrial_pollution_flag * 12
+ multi_system_damage_flag * 16
+ ecological_damage_flag * 16
+ severity_class * 8
- conceptual_flag * 20

if air_pollution_flag = 1 and industrial_pollution_flag = 1:
mixed_raw_score = mixed_raw_score + 8

if mining_impact_flag = 1 and ecological_damage_flag = 1:
mixed_raw_score = mixed_raw_score + 9

if conceptual_flag = 1 and ecological_damage_flag = 0:
mixed_raw_score = mixed_raw_score / 2

mixed_domain_score =
average(all mixed_raw_score)

if mixed_domain_score > 75:
mixed_domain_score = mixed_domain_score + 5



domain_pressure_score =
round(
water_domain_score * 0.30
+ soil_domain_score * 0.25
+ forest_domain_score * 0.25
+ mixed_domain_score * 0.20
)

cross_domain_penalty = 0

if water_domain_score > 82 and soil_domain_score > 78:
cross_domain_penalty = cross_domain_penalty + 10

if forest_domain_score > 80 and mixed_domain_score > 74:
cross_domain_penalty = cross_domain_penalty + 8

if water_domain_score > 85 and forest_domain_score > 75:
cross_domain_penalty = cross_domain_penalty + 6

if retrieval_score > 40:
cross_domain_penalty = cross_domain_penalty + 5

final_synthesis_value =
domain_pressure_score
+ cross_domain_penalty
- retrieval_score

Return JSON only.