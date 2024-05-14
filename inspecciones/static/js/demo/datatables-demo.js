// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    layout: {
top1Start: {
    buttons: [
        {
            extend: 'copy',
            text: 'Copiar',
            titleAttr: 'Copiar'
        },
        {
            extend: 'excel',
            text: 'Excel',
            titleAttr: 'Excel',
            className: '',
        },
        {
            extend: 'print',
            text: 'Imprimir',
            titleAttr: 'Imprimir',
            download: 'open'
        }
    ]
}
},
    "language": {
        "url": "https://cdn.datatables.net/plug-ins/1.10.24/i18n/Spanish.json"
    }
}
);
});
