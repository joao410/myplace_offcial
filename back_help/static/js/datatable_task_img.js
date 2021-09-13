$(document).ready(function() {
    $('#table_task_img').DataTable({
    "pageLength" : 5,
    "lengthMenu": [[5, 10, 20, 50, -1], [5, 10, 20, 50, 'Todas']],
    "order": [[ 0, "desc" ]],
    "language": {
    "sSearch": "Buscar:",
    "sInfo": "Tarefas de _START_ a _END_ (Total _MAX_)",
    "sInfoEmpty": "0 Tarefas",
    "sInfoFiltered": "(filtrado de um total de _MAX_ Tarefas)",
    "sLengthMenu": "Mostrar _MENU_ tarefas",
    "sZeroRecords": "Nenhuma tarefa encontrado",
    "sEmptyTable": "Zero Tarefas",
    "paginate": {
    "previous": "Anterior",
    "next": "Próxima"
    }
}
} );
} );