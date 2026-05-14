{% extends 'base.html' %}

{% block content %}
<section class="form-section">
    <div class="form-card">
        <div class="form-header">
            <div class="form-icon">⚽</div>
            <h2>{{ titulo }}</h2>
            <p>Copa do Mundo 2026</p>
        </div>

        <form method="POST" action="/{{ action }}">
            <div class="form-group">
                <label for="selecao">🌍 Seleção *</label>
                <input
                    type="text"
                    id="selecao"
                    name="selecao"
                    placeholder="Ex: Brasil, Argentina, França..."
                    value="{{ selecao.selecao if selecao else '' }}"
                    required
                >
            </div>

            <div class="form-group">
                <label for="continente">🗺️ Continente *</label>
                <select id="continente" name="continente" required>
                    <option value="">Selecione o continente...</option>
                    {% set continentes = ['América do Sul', 'América do Norte', 'Europa', 'África', 'Ásia', 'Oceania'] %}
                    {% for c in continentes %}
                    <option value="{{ c }}" {% if selecao and selecao.continente == c %}selected{% endif %}>
                        {{ c }}
                    </option>
                    {% endfor %}
                </select>
            </div>

            <div class="form-group">
                <label for="titulos">🏆 Número de Títulos Mundiais</label>
                <input
                    type="number"
                    id="titulos"
                    name="titulos"
                    min="0"
                    max="10"
                    placeholder="0"
                    value="{{ selecao.titulos if selecao else '0' }}"
                >
            </div>

            <div class="form-actions">
                <a href="{{ url_for('index') }}" class="btn-secondary">← Cancelar</a>
                <button type="submit" class="btn-primary">
                    {% if selecao %}💾 Salvar Alterações{% else %}✅ Cadastrar Seleção{% endif %}
                </button>
            </div>
        </form>
    </div>
</section>
{% endblock %}
