$(document).ready(function () {
  $(".datatable").DataTable({
    "language": {
    "sSearch": "Buscar:",
    "sInfo": "Chamados de _START_ a _END_ (Total _MAX_)",
    "sInfoEmpty": "0 chamados",
    "sInfoFiltered": "(filtrado de um total de _MAX_ chamados)",
    "sLengthMenu": "Mostrar _MENU_ chamados",
    "sZeroRecords": "Nenhum chamado encontrado",
    "sEmptyTable": "Zero chamados",
    "paginate": {
    "previous": "Anterior",
    "next": "Próxima"
    },   
}
}),
    $(".dataTables_length select").addClass("form-select form-select-sm");
});
