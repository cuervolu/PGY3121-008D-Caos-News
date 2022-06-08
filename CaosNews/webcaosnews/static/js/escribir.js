
const useDarkMode = window.matchMedia('(prefers-color-scheme: white)').matches;
const isSmallScreen = window.matchMedia('(max-width: 1023.5px)').matches;

tinymce.init({
    selector: 'textarea',
    language: 'es',
    plugins: 'preview importcss searchreplace autolink autosave save directionality code visualblocks visualchars fullscreen  link template codesample table charmap pagebreak nonbreaking anchor insertdatetime advlist lists wordcount help charmap quickbars emoticons code',
    menubar: 'file edit view insert format tools table help',
    toolbar: 'undo redo | bold italic underline strikethrough | fontfamily fontsize blocks | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist | forecolor backcolor removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | template link anchor codesample | ltr rtl | code',
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
    contextmenu: 'link table',
    skin: useDarkMode ? 'oxide-dark' : 'oxide',
    content_css: useDarkMode ? 'dark' : 'default',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:16px }',
    setup: function (ed) {
        ed.on("blur", function () {
            $("#" + ed.id).val(tinyMCE.activeEditor.getContent());
        })
    },
});
