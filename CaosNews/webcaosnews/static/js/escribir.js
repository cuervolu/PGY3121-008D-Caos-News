
const isSmallScreen = window.matchMedia('(max-width: 1023.5px)').matches;

tinymce.init({
    selector: 'textarea',
    language: 'es',
    content_style: "@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap'); body { font-family: Fira Sans; font-size: 18pt; };",
    formats: {
        // Changes the default format for h1 to have a class of heading
        h1: { block: 'h1', classes: 'heading',styles: { 'font-weight': 'bold', 'color':'#DC3545'} },
        h2: { block: 'h2', classes: 'heading',styles: { 'font-weight': 'bold', 'color':'#DC3545'} },
        h3: { block: 'h3', classes: 'heading',styles: { 'font-weight': 'bold', 'color':'#DC3545'} },
        h4: { block: 'h4', classes: 'heading',styles: { 'font-weight': 'bold', 'color':'#DC3545'} },
        h5: { block: 'h5', classes: 'heading',styles: { 'font-weight': 'bold', 'color':'#DC3545'} },
        h6: { block: 'h6', classes: 'heading',styles: { 'font-weight': 'bold', 'color':'#DC3545'} },
        bold: { inline: 'span', styles: { 'font-weight': 'bold', 'color':'#DC3545'} }
      },
    plugins: 'preview importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen  link template codesample table charmap pagebreak nonbreaking anchor insertdatetime advlist lists wordcount help charmap quickbars emoticons code',
    menubar: 'file edit view insert format tools table help',
    toolbar: 'insertfile image undo redo | bold italic underline strikethrough | fontfamily fontsize blocks | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | template link anchor codesample | ltr rtl | code',
    toolbar_sticky: true,
    toolbar_sticky_offset: isSmallScreen ? 102 : 108,
    autosave_ask_before_unload: true,
    autosave_interval: '30s',
    autosave_prefix: '{path}{query}-{id}-',
    autosave_restore_when_empty: false,
    autosave_retention: '2m',
    entity_encoding: 'text',
    content_langs: [
        { title: 'English', code: 'en' },
        { title: 'Spanish', code: 'es' }
    ],
    link_list: [
        { title: 'My page 1', value: 'https://www.tiny.cloud' },
        { title: 'My page 2', value: 'http://www.moxiecode.com' }
    ],
    importcss_append: true,
    templates: [
        { title: 'New Table', description: 'creates a new table', content: '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>' },
        { title: 'Starting my story', description: 'A cure for writers block', content: 'Once upon a time...' },
        { title: 'New list with dates', description: 'New List with dates', content: '<div class="mceTmpl"><span class="cdate">cdate</span><br><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>' }
    ],
    template_cdate_format: '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
    template_mdate_format: '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
    height: 600,
    quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quicktable',
    noneditable_class: 'mceNonEditable',
    toolbar_mode: 'sliding',
    contextmenu: 'link table image imagetools',
    style_formats: [
        { title: 'Custom format', format: 'customformat' },
        { title: 'Align left', format: 'alignleft' },
        { title: 'Align center', format: 'aligncenter' },
        { title: 'Align right', format: 'alignright' },
        { title: 'Align full', format: 'alignfull' },
        { title: 'Negrita', inline: 'strong', styles: { color: '#DC3545' } },
        { title: 'Enlace', inline: 'a', styles: { color: '#DC3545' } },
        { title: 'Encabezado 1', block: 'h1', styles: { color: '#DC3545' } },
        { title: 'Encabezado 2', block: 'h2', styles: { color: '#DC3545' } },
        { title: 'Encabezado 3', block: 'h3', styles: { color: '#DC3545' } },
        { title: 'Badge', inline: 'span', styles: { display: 'inline-block', border: '1px solid #DC3545', 'border-radius': '5px', padding: '2px 5px', margin: '0 2px', color: '#DC3545' } },
        { title: 'Table row 1', selector: 'tr', classes: 'tablerow1' },
        { title: 'Image formats' },
        { title: 'Image Left', selector: 'img', styles: { 'float': 'left', 'margin': '0 10px 0 10px' } },
        { title: 'Image Right', selector: 'img', styles: { 'float': 'right', 'margin': '0 0 10px 10px' } },
      ],
    setup: function (ed) {
        ed.on("blur", function () {
            $("#" + ed.id).val(tinyMCE.activeEditor.getContent());
        })
    },
});
