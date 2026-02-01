<template>
  <div id="app">
    <header>
      <h1>🧮 Math Dashboard</h1>
      <p class="subtitle">Select an operation, provide inputs, and get results.</p>
    </header>

    <div class="layout">
      <aside class="sidebar">
        <h3>Operations</h3>
        <ul>
          <li
            v-for="op in operations"
            :key="op.key"
            :class="{ active: selected?.key === op.key }"
            @click="selectOperation(op)"
          >
            {{ op.label }}
          </li>
        </ul>
      </aside>

      <main class="content">
        <div v-if="selected" class="card">
          <h2>{{ selected.label }}</h2>
          <p class="description">{{ selected.description }}</p>

          <form @submit.prevent="calculate">
            <div v-for="param in selected.params" :key="param.name" class="field">
              <label :for="param.name">{{ param.label }}</label>
              <input
                :id="param.name"
                v-model.number="inputs[param.name]"
                type="number"
                :step="param.type === 'float' ? 'any' : '1'"
                required
              />
            </div>

            <button type="submit" :disabled="loading">
              {{ loading ? 'Calculating...' : 'Calculate' }}
            </button>
          </form>

          <div v-if="result !== null" class="result success">
            <strong>Result:</strong> {{ result }}
          </div>

          <div v-if="error" class="result error">
            <strong>Error:</strong> {{ error }}
          </div>
        </div>

        <div v-else class="card placeholder">
          <p>← Select an operation from the sidebar</p>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, watch } from 'vue'

const API_BASE = import.meta.env.VITE_API_URL || '/api'

const operations = ref([])
const selected = ref(null)
const inputs = reactive({})
const result = ref(null)
const error = ref(null)
const loading = ref(false)

async function fetchOperations() {
  try {
    const res = await fetch(`${API_BASE}/operations`)
    operations.value = await res.json()
    if (operations.value.length > 0) {
      selectOperation(operations.value[0])
    }
  } catch (e) {
    console.error('Failed to fetch operations:', e)
  }
}

function selectOperation(op) {
  selected.value = op
  result.value = null
  error.value = null
  // Reset inputs with defaults
  Object.keys(inputs).forEach(k => delete inputs[k])
  for (const param of op.params) {
    inputs[param.name] = param.default ?? 0
  }
}

async function calculate() {
  if (!selected.value) return
  loading.value = true
  result.value = null
  error.value = null

  try {
    const res = await fetch(`${API_BASE}/calculate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        operation: selected.value.key,
        params: { ...inputs },
      }),
    })

    const data = await res.json()

    if (!res.ok) {
      error.value = data.detail || 'Unknown error'
    } else {
      result.value = data.result
    }
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

fetchOperations()
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #0f172a;
  color: #e2e8f0;
  min-height: 100vh;
}

#app {
  max-width: 960px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

header {
  text-align: center;
  margin-bottom: 2rem;
}

header h1 {
  font-size: 2rem;
  color: #f1f5f9;
}

.subtitle {
  color: #94a3b8;
  margin-top: 0.5rem;
}

.layout {
  display: flex;
  gap: 1.5rem;
}

.sidebar {
  min-width: 180px;
  background: #1e293b;
  border-radius: 12px;
  padding: 1rem;
}

.sidebar h3 {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #64748b;
  margin-bottom: 0.75rem;
}

.sidebar ul {
  list-style: none;
}

.sidebar li {
  padding: 0.6rem 0.8rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.15s;
  font-size: 0.95rem;
}

.sidebar li:hover {
  background: #334155;
}

.sidebar li.active {
  background: #3b82f6;
  color: #fff;
  font-weight: 600;
}

.content {
  flex: 1;
}

.card {
  background: #1e293b;
  border-radius: 12px;
  padding: 1.5rem;
}

.card h2 {
  font-size: 1.4rem;
  margin-bottom: 0.25rem;
}

.description {
  color: #94a3b8;
  margin-bottom: 1.25rem;
}

.field {
  margin-bottom: 1rem;
}

.field label {
  display: block;
  font-size: 0.85rem;
  color: #94a3b8;
  margin-bottom: 0.3rem;
}

.field input {
  width: 100%;
  padding: 0.6rem 0.8rem;
  border: 1px solid #334155;
  border-radius: 8px;
  background: #0f172a;
  color: #e2e8f0;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.15s;
}

.field input:focus {
  border-color: #3b82f6;
}

button {
  padding: 0.7rem 1.5rem;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

button:hover {
  background: #2563eb;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.result {
  margin-top: 1.25rem;
  padding: 1rem;
  border-radius: 8px;
  font-size: 1.05rem;
}

.result.success {
  background: #064e3b;
  color: #6ee7b7;
}

.result.error {
  background: #7f1d1d;
  color: #fca5a5;
}

.placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 200px;
  color: #64748b;
}

@media (max-width: 640px) {
  .layout {
    flex-direction: column;
  }
  .sidebar {
    min-width: unset;
  }
  .sidebar ul {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }
  .sidebar li {
    padding: 0.4rem 0.7rem;
    font-size: 0.85rem;
  }
}
</style>
