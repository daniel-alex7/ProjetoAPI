import functions_framework
from flask import jsonify
from services.swapi_service import SwapiService
from utils.filters import sort_results

service = SwapiService()

@functions_framework.http
def starwars(request):
    """
    Endpoint principal da API Star Wars
    """

    resource = request.args.get("resource")
    search = request.args.get("search")
    sort = request.args.get("sort")
    include = request.args.get("include")

    if not resource:
        return jsonify({
            "error": "Parâmetro 'resource' é obrigatório"
        }), 400

    try:
        data = service.get_resource(resource, search)

        # Ordenação
        if sort and "results" in data:
            data["results"] = sort_results(data["results"], sort)

        # Dados correlacionados
        if include and data.get("results"):
            for item in data["results"]:
                if include in item:
                    related_urls = item.get(include, [])
                    item[f"{include}_details"] = service.get_related(related_urls)

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": "Erro ao processar requisição",
            "details": str(e)
        }), 500
