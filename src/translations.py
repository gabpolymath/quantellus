TRANSLATIONS = {
    "en": {
        # 1. Header & Navigation
        "title": "Quantellus",
        "subtitle": "Geospatial Intelligence & Supply Analytics",
        
        # 2. Input Form & Asset Selection
        "select_asset": "Select Commodity",
        "select_placeholder": "Select a commodity",
        "btn_submit": "Run Analysis",
        "validation_select": "Please select a commodity from the list.",
        
        # 3. Commodity Asset Names
        "comm_grano": "Wheat",
        "comm_mais": "Corn",
        "comm_soia": "Soybeans",
        
        # 4. Results Grid Overview Metrics
        "global_ndvi": "Avg NDVI",
        "live_price": "Live Price",
        "daily_change": "Daily Change",
        "volume": "Daily Traded Volume",
        
        # 5. Geospatial Region Details
        "coords": "Coords",
        "date": "Date",
        "local_ndvi": "Local NDVI",
        "region_wheat_1": "Black Sea Basin (Odesa)",
        "region_wheat_2": "Northern Plains (North Dakota, USA)",
        "region_corn_1": "US Corn Belt (Iowa)",
        "region_corn_2": "US Corn Belt (Illinois)",
        "region_soy_1": "Mato Grosso (Sorriso, Brazil)",
        "region_soy_2": "Rosario Area (Argentina)",
        "click_enlarge": "Click to enlarge the satellite image",
        
        # 6. Financial Chart Section
        "market_trend": "Futures Trend",
        "candles": "Candles",
        "line": "Line",
        "no_chart_data": "Financial data unavailable. Configure yfinance to populate this chart.",
        
        # 7. Analysis Signal & Market Drivers
        "macro_driver": "Market Driver Analysis",
        "status_buy": "Supply Pressure (Low Biomass Density)",
        "mot_buy": "The aggregate NDVI shows biomass density falling below historical norms. This indicator of restricted upcoming supply acts as a bullish driver for {ticker} futures.",
        "status_sell": "Surplus Outlook (High Biomass Density)",
        "mot_sell": "Satellite data reveals high biomass density across strategic regions. The projected abundance in production is expected to exert downward pressure on {ticker} prices.",
        
        # 8. Information Modal (About Section)
        "about_title": "What is Quantellus?",
        "about_description": "Quantellus is a geospatial intelligence tool designed to bridge the gap between satellite data and financial markets. By tracking the NDVI (Normalized Difference Vegetation Index) — a metric that measures crop health and biomass density via satellite imagery — Quantellus detects early signs of supply shocks or record yields. The algorithm processes raw raster data from Copernicus across strategic global agricultural basins and correlates it with live futures prices, generating quantitative indicators to help analyze market drivers.",
        "about_note": "NOTE: This is a portfolio project built for educational purposes; as it is not a commercial software nor a replacement for current professional tools, the raster data used is historical from 2025.",
        "github_btn": "View on GitHub",
        
        # 9. Footer Section
        "footer_disclaimer": "Disclaimer: The information provided does not constitute financial advice. Trading futures carries a high level of risk.",
        "footer_copyright": "Quantellus. All rights reserved.",
        
        # 10. Backend Logging & Error Exceptions
        "error_log": "Error Log",
        "err_invalid_commodity": "Invalid Commodity.",
        "err_ndvi_invalid": "No valid NDVI data found in the range [-1, 1]",
        "log_cache_hit": "[CACHE HIT] Returning cached data for {ticker}",
        "log_cache_miss": "[CACHE MISS] Live request to Yahoo Finance for ticker: {ticker}",
        "log_fin_error": "[Error] Unable to retrieve financial data for {ticker}: {error}",
        "log_tiff_warning": "[Warning] Unable to read {tiff_path}. Fallback to default. Error: {error}"
    },
    "it": {
        # 1. Header & Navigation
        "title": "Quantellus",
        "subtitle": "Intelligence Geospaziale e Analisi dell'Offerta",
        
        # 2. Input Form & Asset Selection
        "select_asset": "Seleziona Commodity",
        "select_placeholder": "Seleziona una commodity",
        "btn_submit": "Avvia Analisi",
        "validation_select": "Seleziona una commodity dall'elenco.",
        
        # 3. Commodity Asset Names
        "comm_grano": "Grano",
        "comm_mais": "Mais",
        "comm_soia": "Soia",
        
        # 4. Results Grid Overview Metrics
        "global_ndvi": "NDVI Medio",
        "live_price": "Prezzo Live",
        "daily_change": "Variazione Odierna",
        "volume": "Volume Scambi (Giornaliero)",
        
        # 5. Geospatial Region Details
        "coords": "Coordinate",
        "date": "Data",
        "local_ndvi": "NDVI Locale",
        "region_wheat_1": "Bacino del Mar Nero (Odessa)",
        "region_wheat_2": "Pianure Settentrionali (Nord Dakota, USA)",
        "region_corn_1": "Corn Belt USA (Iowa)",
        "region_corn_2": "Corn Belt USA (Illinois)",
        "region_soy_1": "Mato Grosso (Sorriso, Brasile)",
        "region_soy_2": "Area di Rosario (Argentina)",
        "click_enlarge": "Clicca per ingrandire l'immagine satellitare",
        
        # 6. Financial Chart Section
        "market_trend": "Andamento Futures",
        "candles": "Candele",
        "line": "Linea",
        "no_chart_data": "Dati finanziari non disponibili. Configura lo storico dati yfinance per popolare questo grafico.",
        
        # 7. Analysis Signal & Market Drivers
        "macro_driver": "Analisi Driver di Mercato",
        "status_buy": "Pressione sull'Offerta (Bassa Densità di Biomassa)",
        "mot_buy": "L'NDVI aggregato mostra una densità di biomassa inferiore alle norme storiche. Questo indicatore di offerta limitata agisce come driver rialzista per i futures {ticker}.",
        "status_sell": "Prospettive di Surplus (Alta Densità di Biomassa)",
        "mot_sell": "I dati satellitari rivelano un'alta densità di biomassa nelle regioni strategiche. L'abbondanza di produzione prevista dovrebbe esercitare una pressione ribassista sui prezzi di {ticker}.",
        
        # 8. Information Modal (About Section)
        "about_title": "Cos'è Quantellus?",
        "about_description": "Quantellus è uno strumento di intelligence geospaziale progettato per unire i dati satellitari e i mercati finanziari. Monitorando l'indice NDVI — che misura la salute delle colture e la densità della biomassa tramite immagini satellitari — Quantellus rileva in anticipo i segnali di crisi dell'offerta o di raccolti record. L'algoritmo elabora i dati raster grezzi provenienti da Copernicus per i principali bacini agricoli globali e li correla con i prezzi dei futures in tempo reale, generando indicatori quantitativi per l'analisi dei mercati.",
        "about_note": "NOTA: Questo progetto ha scopi didattici e di portfolio; non essendo un software commerciale né un sostituto per gli strumenti professionali attuali, i dati raster utilizzati sono storici e risalgono al 2025.",
        "github_btn": "Vedi su GitHub",
        
        # 9. Footer Section
        "footer_disclaimer": "Disclaimer: Le informazioni fornite non costituiscono consulenza finanziaria. Il trading di futures comporta un alto rischio di perdita.",
        "footer_copyright": "Quantellus. Tutti i diritti riservati.",
        
        # 10. Backend Logging & Error Exceptions
        "error_log": "Log Errore",
        "err_invalid_commodity": "Commodity non valida.",
        "err_ndvi_invalid": "Nessun dato NDVI valido trovato nel range [-1, 1]",
        "log_cache_hit": "[CACHE HIT] Restituisco i dati memorizzati per {ticker}",
        "log_cache_miss": "[CACHE MISS] Richiesta live a Yahoo Finance per il ticker: {ticker}",
        "log_fin_error": "[Error] Impossibile recuperare i dati finanziari per {ticker}: {error}",
        "log_tiff_warning": "[Warning] Impossibile leggere {tiff_path}. Fallback a default. Error: {error}"
    }
}