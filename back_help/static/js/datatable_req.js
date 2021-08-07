$(document).ready(function() {
    $('#datatable_req').DataTable({
    "pageLength" : 5,
    "lengthMenu": [[5, 10, 20, 50, -1], [5, 10, 20, 50, 'Todas']],
    "order": [[ 0, "desc" ]],
    "language": {
    "sSearch": "Buscar:",
    "sInfo": "requisições de _START_ a _END_ (Total _MAX_)",
    "sInfoEmpty": "0 requisições",
    "sInfoFiltered": "(filtrado de um total de _MAX_ requisições)",
    "sLengthMenu": "Mostrar _MENU_ requisições",
    "sZeroRecords": "Nenhuma tarefa encontrado",
    "sEmptyTable": "Zero requisições",
    "paginate": {
    "previous": "Anterior",
    "next": "Próxima"
    }
}
} );
} );



