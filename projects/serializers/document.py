from django.urls import reverse
from rest_framework import serializers

from projects.models import DocumentTemplate


class DocumentTemplateSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    phase_name = serializers.SlugField(source="common_project_phase.prefixed_name", read_only=True)
    phase_index = serializers.SerializerMethodField()
    phase_ended = serializers.SerializerMethodField()

    class Meta:
        model = DocumentTemplate
        fields = [
            "id",
            "name",
            "image_template",
            "file",
            "phase_name",
            "phase_index",
            "phase_ended",
        ]
        read_only_fields = ["id", "name", "image_template"]

    def get_file(self, document_template):
        request = self.context["request"]
        project_id = self.context["project"].id
        url = reverse(
            "documenttemplate-detail",
            kwargs={"project_pk": project_id, "slug": document_template.slug},
        )
        absolute_url = request.build_absolute_uri(url)
        return absolute_url

    def get_phase_ended(self, document_template):
        project_phase = document_template.common_project_phase.phases.get(
            project_subtype=self.context["project"].subtype,
        )
        return project_phase.index < \
            self.context["project"].phase.index

    def get_phase_index(self, document_template):
        project_phase = document_template.common_project_phase.phases.get(
            project_subtype=self.context["project"].subtype,
        )
        return project_phase.index
