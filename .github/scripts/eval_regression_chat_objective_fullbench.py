from mmengine.config import read_base

with read_base():
    # read hf models - chat models
    # Dataset
    from opencompass.configs.datasets.ARC_c.ARC_c_cot_gen_926652 import \
        ARC_c_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.bbh.bbh_gen_5b92b0 import \
        bbh_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.cmmlu.cmmlu_0shot_cot_gen_305931 import \
        cmmlu_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.drop.drop_openai_simple_evals_gen_3857b0 import \
        drop_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.ds1000.ds1000_service_eval_gen_cbc84f import \
        ds1000_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.GaokaoBench.GaokaoBench_no_subjective_gen_4c31db import \
        GaokaoBench_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.gpqa.gpqa_openai_simple_evals_gen_5aeece import \
        gpqa_datasets  # noqa: F401, E501
    # new datasets in Fullbench v1.1
    from opencompass.configs.datasets.gsm8k.gsm8k_0shot_v2_gen_a58960 import \
        gsm8k_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.hellaswag.hellaswag_10shot_gen_e42710 import \
        hellaswag_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.humaneval.humaneval_openai_sample_evals_gen_159614 import \
        humaneval_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.humanevalx.humanevalx_gen_620cfa import \
        humanevalx_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.IFEval.IFEval_gen_3321a3 import \
        ifeval_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.math.math_0shot_gen_393424 import \
        math_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.MathBench.mathbench_2024_gen_50a320 import \
        mathbench_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.mbpp.sanitized_mbpp_mdblock_gen_a447ff import \
        sanitized_mbpp_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.mmlu.mmlu_openai_simple_evals_gen_b618ea import \
        mmlu_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.mmlu_pro.mmlu_pro_0shot_cot_gen_08c1de import \
        mmlu_pro_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.nq.nq_open_1shot_gen_2e45e5 import \
        nq_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.race.race_cot_gen_d95929 import \
        race_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.scicode.scicode_gen_085b98 import \
        SciCode_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.SuperGLUE_BoolQ.SuperGLUE_BoolQ_cot_gen_1d56df import \
        BoolQ_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.teval.teval_en_gen_1ac254 import \
        teval_datasets as teval_en_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.teval.teval_zh_gen_1ac254 import \
        teval_datasets as teval_zh_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.TheoremQA.TheoremQA_5shot_gen_6f0af8 import \
        TheoremQA_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.triviaqa.triviaqa_wiki_1shot_gen_bc5f21 import \
        triviaqa_datasets  # noqa: F401, E501
    from opencompass.configs.datasets.wikibench.wikibench_gen_0978ad import \
        wikibench_datasets  # noqa: F401, E501
    from opencompass.configs.models.hf_internlm.hf_internlm2_5_7b_chat import \
        models as hf_internlm2_5_7b_chat_model  # noqa: F401, E501
    from opencompass.configs.models.hf_internlm.lmdeploy_internlm2_5_7b_chat import \
        models as lmdeploy_internlm2_5_7b_chat_model  # noqa: F401, E501
    # Summary Groups
    from opencompass.configs.summarizers.groups.bbh import \
        bbh_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.cmmlu import \
        cmmlu_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.ds1000 import \
        ds1000_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.GaokaoBench import \
        GaokaoBench_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.humanevalx import \
        humanevalx_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.mathbench_v1_2024 import \
        mathbench_2024_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.mmlu import \
        mmlu_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.mmlu_pro import \
        mmlu_pro_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.scicode import \
        scicode_summary_groups  # noqa: F401, E501
    from opencompass.configs.summarizers.groups.teval import \
        teval_summary_groups  # noqa: F401, E501

# For HumanEval-X Evaluation
# Apply the evaluator ip_address and port
race_datasets = [race_datasets[1]]
for item in humanevalx_datasets:
    item['eval_cfg']['evaluator'][
        'ip_address'] = 'codeeval.opencompass.org.cn/humanevalx'
    item['eval_cfg']['evaluator']['port'] = ''

# For DS-1000 Evaluation
# Apply the evaluator ip_address and port
for item in ds1000_datasets:
    item['eval_cfg']['evaluator'][
        'ip_address'] = 'codeeval.opencompass.org.cn/ds1000'
    item['eval_cfg']['evaluator']['port'] = ''

bbh_datasets = [
    x for x in bbh_datasets if 'logical_deduction_seven_objects' in x['abbr']
    or 'multistep_arithmetic_two' in x['abbr']
]
cmmlu_datasets = [
    x for x in cmmlu_datasets if x['abbr'].replace('cmmlu-', '') in [
        'ancient_chinese', 'chinese_civil_service_exam',
        'chinese_driving_rule', 'chinese_food_culture',
        'chinese_foreign_policy', 'chinese_history', 'chinese_literature',
        'chinese_teacher_qualification', 'construction_project_management',
        'elementary_chinese', 'elementary_commonsense', 'ethnology',
        'high_school_politics', 'modern_chinese',
        'traditional_chinese_medicine'
    ]
]
mmlu_datasets = [
    x for x in mmlu_datasets if x['abbr'].replace('lukaemon_mmlu_', '') in [
        'business_ethics', 'clinical_knowledge', 'college_medicine',
        'global_facts', 'human_aging', 'management', 'marketing',
        'medical_genetics', 'miscellaneous', 'nutrition',
        'professional_accounting', 'professional_medicine', 'virology'
    ]
]

mmlu_pro_datasets = [mmlu_pro_datasets[0]]
mathbench_datasets = [x for x in mathbench_datasets if 'college' in x['abbr']]
GaokaoBench_datasets = [
    x for x in GaokaoBench_datasets if '2010-2022_Math_II_MCQs' in x['abbr']
    or '2010-2022_Math_II_Fill-in-the-Blank' in x['abbr']
]

datasets = sum(
    (v for k, v in locals().items() if k.endswith('_datasets')
     and 'scicode' not in k.lower() and 'teval' not in k),
    [],
)
datasets += teval_en_datasets
datasets += teval_zh_datasets
# datasets += SciCode_datasets

summarizer = dict(
    dataset_abbrs=[
        ['race-high', 'accuracy'],
        ['ARC-c', 'accuracy'],
        ['BoolQ', 'accuracy'],
        ['mmlu_pro', 'naive_average'],
        ['drop', 'accuracy'],
        ['bbh', 'naive_average'],
        ['GPQA_diamond', 'accuracy'],
        ['math', 'accuracy'],
        ['wikibench-wiki-single_choice_cncircular', 'perf_4'],
        ['openai_humaneval', 'humaneval_pass@1'],
        ['sanitized_mbpp', 'score'],
        ['cmmlu', 'naive_average'],
        ['mmlu', 'naive_average'],
        ['teval', 'naive_average'],
        ['SciCode', 'accuracy'],
        ['SciCode', 'sub_accuracy'],
        ['humanevalx', 'naive_average'],
        ['ds1000', 'naive_average'],
        ['IFEval', 'Prompt-level-strict-accuracy'],
        ['gsm8k', 'accuracy'],
        ['GaokaoBench', 'weighted_average'],
        ['triviaqa_wiki_1shot', 'score'],
        ['nq_open_1shot', 'score'],
        ['hellaswag', 'accuracy'],
        ['TheoremQA', 'score'],
        '###### MathBench-A: Application Part ######',
        'college',
        'high',
        'middle',
        'primary',
        'arithmetic',
        'mathbench-a (average)',
        '###### MathBench-T: Theory Part ######',
        'college_knowledge',
        'high_knowledge',
        'middle_knowledge',
        'primary_knowledge',
        'mathbench-t (average)',
        '###### Overall: Average between MathBench-A and MathBench-T ######',
        'Overall',
        '',
        'bbh-logical_deduction_seven_objects',
        'bbh-multistep_arithmetic_two',
        ''
        'mmlu',
        'mmlu-stem',
        'mmlu-social-science',
        'mmlu-humanities',
        'mmlu-other',
        '',
        'cmmlu',
        'cmmlu-stem',
        'cmmlu-social-science',
        'cmmlu-humanities',
        'cmmlu-other',
        'cmmlu-china-specific',
        '',
        'mmlu_pro',
        'mmlu_pro_biology',
        'mmlu_pro_business',
        'mmlu_pro_chemistry',
        'mmlu_pro_computer_science',
        'mmlu_pro_economics',
        'mmlu_pro_engineering',
        'mmlu_pro_health',
        'mmlu_pro_history',
        'mmlu_pro_law',
        'mmlu_pro_math',
        'mmlu_pro_philosophy',
        'mmlu_pro_physics',
        'mmlu_pro_psychology',
        'mmlu_pro_other',
        '',
        'GaokaoBench_2010-2022_Math_II_MCQs',
        'GaokaoBench_2010-2022_Math_II_Fill-in-the-Blank',
        '',
        'humanevalx-python',
        'humanevalx-cpp',
        'humanevalx-go',
        'humanevalx-java',
        'humanevalx-js',
        '',
        'ds1000_Pandas',
        'ds1000_Numpy',
        'ds1000_Tensorflow',
        'ds1000_Scipy',
        'ds1000_Sklearn',
        'ds1000_Pytorch',
        'ds1000_Matplotlib',
    ],
    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)

for d in datasets:
    d['reader_cfg']['test_range'] = '[0:16]'

models = sum([v for k, v in locals().items() if k.endswith('_model')], [])
for m in models:
    m['abbr'] = m['abbr'] + '_fullbench'
    if 'turbomind' in m['abbr'] or 'lmdeploy' in m['abbr']:
        m['engine_config']['max_batch_size'] = 1
        m['batch_size'] = 1

models = sorted(models, key=lambda x: x['run_cfg']['num_gpus'])
