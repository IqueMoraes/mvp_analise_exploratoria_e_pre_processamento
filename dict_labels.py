dict_labels = {
    'id_estudante': ("Id do estudante", {}),
    'idade': (
        "Idade", {
            1: '18-21',
            2: '22-25',
            3: '>=26',
        }
    ),
    'genero': (
        "Gênero", {
            1: 'mulher',
            2: 'homem',
        }
    ),
    'natureza_graduacao': (
        "Natureza da graduação", {
            1: 'privada',
            2: 'público',
            3: 'outra',
        }
    ),
    'bolsa_estudo': (
        "Bolsa de estudo concedida", {
            1: '0%',
            2: '25%',
            3: '50%',
            4: '75%',
            5: '100%',
        }
    ),
    'trabalho': (
        "Se possui trabalho remunerado", {
            1: 'sim',
            2: 'não',
        }
    ),
    'atividade_extra': (
        "Se pratica esporte ou arte", {
            1: 'sim',
            2: 'não',
        }
    ),
    'parceiro(a)': (
        "Se possui parceiro(a)", {
            1: 'sim',
            2: 'não',
        }
    ),
    'salario_total': (
        "Soma total do salário quando positivo", {
            1: '135-200',
            2: '201-270',
            3: '271-340',
            4: '341-410',
            5: '>410'
        }
    ),
    'meio_de_transporte': (
        "Meio de transporte para faculdade", {
            1: 'Ônibus',
            2: 'Carro próprio ou táxi',
            3: 'Bicicleta',
            4: 'Outro'
        }
    ),
    'acomodacao': (
        "Tipo de acomodação", {
            1: 'Aluguel',
            2: 'Dormitório',
            3: 'Com a família',
            4: 'Outro'
        }
    ),
    'educacao_mae': (
        "Nível educacional da mãe", {
            1: 'Escola primária',
            2: 'Escola Secundária',
            3: 'Ensino Médio',
            4: 'Graduação',
            5: 'Mestrado',
            6: 'Doutorado'
        }
    ),
    'educacao_pai': (
        "Nível educacional do pai", {
            1: 'Escola primária',
            2: 'Escola Secundária',
            3: 'Ensino Médio',
            4: 'Graduação',
            5: 'Mestrado',
            6: 'Doutorado'
        }
    ),
    'irmaos(as)': (
        "Número de irmão, quando positivo", {
            1: '1',
            2: '2',
            3: '3',
            4: '4',
            5: '>=5'
        }
    ),
    'estado_civil_pais': (
        "Estado civil dos pais", {
            1: 'Casados',
            2: 'Divorciados',
            3: 'Viúvo(a) ou ambos falecidos'
        }
    ),
    'ocupacao_mae': (
        "Ocupação da mãe", {
            1: 'Aposentada',
            2: 'Dona de casa',
            3: 'Trabalhadora do setor público',
            4: 'Trabalhadora do setor privado',
            5: 'Empreendedora',
            6: 'Outra'
        }
    ),
    'ocupacao_pai': (
        "Ocupação do pai", {
            1: 'Aposentado',
            2: 'Trabalhador do setor público',
            3: 'Trabalhador do setor privado',
            4: 'Empreendedor',
            5: 'Outra'
        }
    ),
    'estudo_semanais': (
        "Horas total de estudos semanais", {
            1: '0',
            2: '<=5',
            3: '6-10',
            4: '11-20',
            5: '>=20'
        }
    ),
    'freq_leitura_nao_cientifica': (
        "Frequência de leitura não científica", {
            1: 'Nenhuma',
            2: 'Alguma',
            3: 'Alta',
        }
    ),
    'freq_leitura_cientifica': (
        "Frequência de leitura científica", {
            1: 'Nenhuma',
            2: 'Alguma',
            3: 'Alta',
        }
    ),
    'freq_evento_academico_dpto': (
        "Se frequenta os eventos do dpto.", {
            1: 'sim',
            2: 'não',
        }
    ),
    'impacto_do_projeto_no_sucesso': (
        "Impacto do projeto no sucesso pessoal", {
            1: 'Positivo',
            2: 'Negativo',
            3: 'Neutro',
        }
    ),
    'freq_aula': (
        "Frequência nas aulas regulares", {
            1: 'Sempre',
            2: 'Algumas',
            3: 'Nunca',
        }
    ),
    'estudo_avaliacoes': (
        "Formato de estudos para provas", {
            1: 'Sozinho',
            2: 'Com amigos',
            3: 'Não aplicável',
        }
    ),
    'organizacao_avaliacoes': (
        "Período de estudo para provas", {
            1: 'Próximo ao exame',
            2: 'Regularmente no semestre',
            3: 'Nunca',
        }
    ),
    'anotacoes_nas_aulas': (
        "Frequência de anotações em aula", {
            1: 'Nunca',
            2: 'Algumas vezes',
            3: 'Sempre',
        }
    ),
    'escuta_nas_aulas': (
        "Frequência de atenção em aula", {
            1: 'Nunca',
            2: 'Algumas vezes',
            3: 'Sempre',
        }
    ),
    'melhora_com_debates': (
        "Se os debates ajudam no sucesso do curso", {
            1: 'Nunca',
            2: 'Algumas vezes',
            3: 'Sempre',
        }
    ),
    'utilidade_aula_mista': (
        "Percepção de aulas com técnicas mistas", {
            1: 'Inútil',
            2: 'Útil',
            3: 'Não aplicável',
        }
    ),
    'media_acumulada_ultimo_sem': (
        "Média acumulada no último semestre", {
            1: '<2.00',
            2: '2.00-2.49',
            3: '2.50-2.99',
            4: '3.00-3.49',
            5: '>3.49',
        }
    ),
    'expectativa_media_acumulada': (
        "Expectativa da futura média acumulada", {
            1: '<2.00',
            2: '2.00-2.49',
            3: '2.50-2.99',
            4: '3.00-3.49',
            5: '>3.49',
        }
    ),
    'id_curso': (
        "Id do curso de graduação", {}),
    'grade_notas': (
        "Nota obtida", {
            0: 'Zero',
            1: 'DD',
            2: 'DC',
            3: 'CC',
            4: 'CB',
            5: 'BB',
            6: 'BA',
            7: 'AA',
    }),
}
