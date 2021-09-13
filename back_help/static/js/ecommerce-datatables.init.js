$(document).ready(function () {
  $(".datatable").DataTable({
    "language": {
    "sSearch": "Buscar:",
    "sInfo": "Colaboradores de _START_ a _END_ (Total _MAX_)",
    "sInfoEmpty": "0 colaboradores",
    "sInfoFiltered": "(filtrado de um total de _MAX_ colaboradores)",
    "sLengthMenu": "Mostrar _MENU_ colaboradores",
    "sZeroRecords": "Nenhum colaborador encontrado",
    "sEmptyTable": "Zero Colaboradores",
    "paginate": {
    "previous": "Anterior",
    "next": "Próxima"
    },   
}
}),
    $(".dataTables_length select").addClass("form-select form-select-sm");
});
