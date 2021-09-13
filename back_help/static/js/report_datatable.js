$(document).ready(function() {
  $('#table_report_rh').DataTable({
  "pageLength" : 5,
  "lengthMenu": [[5, 10, 20, 50, -1], [5, 10, 20, 50, 'Todas']],
  "order": [[ 0, "desc" ]],
  "language": {
  "sSearch": "Buscar:",
  "sInfo": "Relatorios de _START_ a _END_ (Total _MAX_)",
  "sInfoEmpty": "0 Relatorios",
  "sInfoFiltered": "(filtrado de um total de _MAX_ Relatorios)",
  "sLengthMenu": "Mostrar _MENU_ relatorios",
  "sZeroRecords": "Nenhum relatorio encontrado",
  "sEmptyTable": "Zero relatorios ",
  "paginate": {
  "previous": "Anterior",
  "next": "Próxima"
  }
}
} ),
    $(".dataTables_length select").addClass("form-select form-select-sm");
});
