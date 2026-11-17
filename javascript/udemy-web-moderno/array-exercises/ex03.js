const turma = [{
    nome: 'Turma M1',
    alunos: [{
        nome: 'Gustavo',
        nota: 8.1,
    }, {
        nome: 'Ana',
        nota: 9.3
    }]
    }, {
        nome: 'Turma M2',
        alunos: [{
            nome: 'Rebeca',
            nota: 8.9
            }, {
            nome: 'Roberta',
            nota: 7.3
            }] 
}]

const getNotaAlunos = aluno =>  aluno.nota
const getNotasDaTurma = turma => turma.nome.alunos.map(getNotaAlunos)

console.log(turma.map(getNotaAlunos))