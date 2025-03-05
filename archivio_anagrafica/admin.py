from django.contrib import admin
from .models import Provincia, Comune, Utente, TitoloStudio, Documento, RegistroUtente
from django.utils.safestring import mark_safe

# Register your models here.

class ProvinciaAdmin(admin.ModelAdmin):
    list_filter = ("nome",)
    
class ComuneAdmin(admin.ModelAdmin):
    list_filter = ("comune",)
    
class UtenteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    class Media:
        js = ()

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name in ['provincia_nascita', 'provincia_residenza']:
            # Aggiungiamo lo stesso script per entrambe le province
            kwargs['help_text'] = mark_safe(f"""
                <script>
                (function($) {{
                    $(function() {{
                        function updateComuni(provinciaFieldId, comuneFieldId) {{
                            var provinciaId = $('#' + provinciaFieldId).val();
                            var comuniSelect = $('#' + comuneFieldId);

                            comuniSelect.empty();
                            comuniSelect.append($('<option>').text('---------').attr('value', ''));

                            if (provinciaId) {{
                                fetch(`/comuni/${{provinciaId}}/`)
                                    .then(response => response.json())
                                    .then(data => {{
                                        data.forEach(function(comune) {{
                                            comuniSelect.append($('<option>').text(comune.comune).attr('value', comune.id));
                                        }});
                                    }});
                            }}
                        }}

                        $('#id_provincia_nascita').change(function() {{
                            updateComuni('id_provincia_nascita', 'id_comune_nascita');
                        }});

                        $('#id_provincia_residenza').change(function() {{
                            updateComuni('id_provincia_residenza', 'id_comune_residenza');
                        }});

                    }});
                }})(django.jQuery);
                </script>
            """)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Comune, ComuneAdmin)
admin.site.register(Utente, UtenteAdmin)
admin.site.register(TitoloStudio)
admin.site.register(Documento)
admin.site.register(RegistroUtente)